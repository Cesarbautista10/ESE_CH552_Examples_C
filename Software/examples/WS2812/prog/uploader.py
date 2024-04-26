import sys
import struct

import usb.core
import usb.util

# ===================================================================================
# Programmer Class
# ===================================================================================

class Programmer:
    def __init__(self):
        dev = usb.core.find(idVendor=CH_VID, idProduct=CH_PID)
        if dev is None:
            raise Exception('ERROR: No CH55x device found!')

        try:
            dev.set_configuration()
        except usb.core.USBError as ex:
            error_msg = 'ERROR: Failed to access USB device.'
            if str(ex).startswith('[Errno 13]') and platform.system() == 'Linux':
                error_msg += ' Configure udev or run as root (sudo).'
            raise Exception(error_msg)

        cfg = dev.get_active_configuration()
        intf = cfg[(0, 0)]

        self.epout = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
        self.epin = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN)
        assert self.epout is not None
        assert self.epin is not None

        self.chipid = 0
        self.chipname = 'CH000'
        self.bootloader = '0.0'
        self.chipversion = 0
        self.device_erase_size = 8
        self.device_flash_size = 16
        self.code_flash_size = 14336

    def detect(self):
        identanswer = self.__sendcmd(DETECT_CHIP_CMD_V2)
        if len(identanswer) == 0:
            raise Exception('Chip identification failed')
        if len(identanswer) == 2:
            self.chipversion = 1
            self.__identchipv1()
        else:
            self.chipversion = 2
            self.__identchipv2()

        self.chipname = 'CH5' + str(self.chipid - 30)
        if self.chipid == 0x51 or self.chipid == 0x53:
            self.code_flash_size = 10240
        elif self.chipid == 0x58:
            self.device_flash_size = 64
            self.device_erase_size = 11
            self.code_flash_size = 32768
        elif self.chipid == 0x59:
            self.device_flash_size = 64
            self.device_erase_size = 11
            self.code_flash_size = 61440

        print('Chip detected:', self.chipname)

    def erase(self):
        if self.chipversion == 1:
            self.__erasev1()
        else:
            self.__erasev2()

        print('Erased successfully')

    def flash_bin(self, filename):
        with open(filename, 'rb') as f:
            data = f.read()
        self.flash_data(data)
        return len(data)

    def verify_bin(self, filename):
        with open(filename, 'rb') as f:
            data = f.read()
        self.verify_data(data)
        return len(data)

    def flash_data(self, data):
        if len(data) > self.code_flash_size:
            raise Exception('Not enough memory')
        if self.chipversion == 1:
            self.__writev1(data, MODE_WRITE_V1)
        else:
            self.__writev2(data, MODE_WRITE_V2)

        print('Flashed successfully')

    def verify_data(self, data):
        if len(data) > self.code_flash_size:
            raise Exception('Not enough memory')
        if self.chipversion == 1:
            self.__writev1(data, MODE_VERIFY_V1)
        else:
            self.__writev2(data, MODE_VERIFY_V2)

        print('Verified successfully')

    def exit(self):
        if self.chipversion == 1:
            self.__exitv1()
        else:
            self.__exitv2()

        print('Exited successfully')

    def __sendcmd(self, cmd):
        self.epout.write(cmd)
        b = self.epin.read(64)
        if len(b) == 2:
            return struct.unpack('<H', b)[0]
        return b

    def __identchipv1(self):
        identanswer = self.__sendcmd(DETECT_CHIP_CMD_V1)
        if len(identanswer) == 2:
            self.chipid = identanswer[0]
        else:
            raise Exception('Wrong chip ID')

        cfganswer = self.__sendcmd((0xbb, 0x00))
        if len(cfganswer) == 2:
            self.bootloader = str(cfganswer[0] >> 4) + '.' + str(cfganswer[0] & 0xf)
        else:
            raise Exception('Wrong bootloader ID')

        print('Chip ID:', self.chipid)
        print('Bootloader version:', self.bootloader)

    def __identchipv2(self):
        identanswer = self.__sendcmd(DETECT_CHIP_CMD_V2)
        if len(identanswer) == 6:
            self.chipid = identanswer[4]
        else:
            raise Exception('Wrong chip ID')

        cfganswer = self.__sendcmd((0xa7, 0x02, 0x00, 0x1f, 0x00))
        if len(cfganswer) == 30:
            self.bootloader = str(cfganswer[19]) + '.' + str(cfganswer[20]) + str(cfganswer[21])
            outbuffer = bytearray(64)
            outbuffer[0] = 0xa3
            outbuffer[1] = 0x30
            outbuffer[2] = 0x00
            checksum = cfganswer[22]
            checksum += cfganswer[23]
            checksum += cfganswer[24]
            checksum += cfganswer[25]
            for x in range(0x30):
                outbuffer[x + 3] = checksum & 0xff
            self.__sendcmd(outbuffer)
        else:
            raise Exception('Wrong bootloader ID')

        print('Chip ID:', self.chipid)
        print('Bootloader version:', self.bootloader)

    def __erasev1(self):
        self.__sendcmd((0xa6, 0x04, 0x00, 0x00, 0x00, 0x00))
        for x in range(self.device_flash_size):
            buffer = self.__sendcmd((0xa9, 0x02, 0x00, x * 4))
            if buffer[0] != 0x00:
                raise Exception('Erase failed')

    def __erasev2(self):
        buffer = self.__sendcmd((0xa4, 0x01, 0x00, self.device_erase_size))
        if buffer[4] != 0x00:
            raise Exception('Erase failed')

    def __exitv1(self):
        self.epout.write((0xa5, 0x02, 0x01, 0x00))

    def __exitv2(self):
        self.epout.write((0xa2, 0x01, 0x00, 0x01))

    def __writev1(self, data, mode):
        rest = len(data)
        curr_addr = 0
        pkt_length = 0
        outbuffer = bytearray(64)
        outbuffer[0] = mode
        while curr_addr < len(data):
            if rest >= 0x3c:
                pkt_length = 0x3c
            else:
                pkt_length = rest
            outbuffer[1] = pkt_length
            outbuffer[2] = (curr_addr & 0xff)
            outbuffer[3] = ((curr_addr >> 8) & 0xff)
            for x in range(pkt_length):
                outbuffer[x + 4] = data[curr_addr + x]
            buffer = self.__sendcmd(outbuffer)
            curr_addr += pkt_length
            rest -= pkt_length
            if buffer is not None:
                if buffer[0] != 0x00:
                    if mode == MODE_WRITE_V1:
                        raise Exception('Write failed')
                    elif mode == MODE_VERIFY_V1:
                        raise Exception('Verify failed')
        return len(data)

    def __writev2(self, data, mode):
        rest = len(data)
        curr_addr = 0
        pkt_length = 0
        outbuffer = bytearray(64)
        outbuffer[0] = mode
        outbuffer[2] = 0x00
        outbuffer[5] = 0x00
        outbuffer[6] = 0x00
        while curr_addr < len(data):
            if rest >= 0x38:
                pkt_length = 0x38
            else:
                pkt_length = rest
            outbuffer[1] = (pkt_length + 5)
            outbuffer[3] = (curr_addr & 0xff)
            outbuffer[4] = ((curr_addr >> 8) & 0xff)
            outbuffer[7] = rest & 0xff
            for x in range(pkt_length):
                outbuffer[x + 8] = data[curr_addr + x]
            for x in range(pkt_length + 8):
                if x % 8 == 7:
                    outbuffer[x] ^= self.chipid
            buffer = self.__sendcmd(outbuffer)
            curr_addr += pkt_length
            rest -= pkt_length
            if buffer is not None:
                if buffer[4] != 0x00 and buffer[4] != 0xfe and buffer[4] != 0xf5:
                    if mode == MODE_WRITE_V2:
                        raise Exception('Write failed')
                    elif mode == MODE_VERIFY_V2:
                        raise Exception('Verify failed')

    # Rest of the Programmer class code ...

# Rest of the code ...

CH_VID = 0x4348
CH_PID = 0x55e0

MODE_WRITE_V1 = 0xa8
MODE_VERIFY_V1 = 0xa7
MODE_WRITE_V2 = 0xa5
MODE_VERIFY_V2 = 0xa6

DETECT_CHIP_CMD_V1 = (0xa2, 0x13, 0x55, 0x53, 0x42, 0x20, 0x44, 0x42, 0x47, 0x20, 0x43, 0x48, 0x35, 0x35, 0x39, 0x20, 0x26, 0x20, 0x49, 0x53, 0x50, 0x00)
DETECT_CHIP_CMD_V2 = (0xa1, 0x12, 0x00, 0x52, 0x11, 0x4d, 0x43, 0x55, 0x20, 0x49, 0x53, 0x50, 0x20, 0x26, 0x20, 0x57, 0x43, 0x48, 0x2e, 0x43, 0x4e)