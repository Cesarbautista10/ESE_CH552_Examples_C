                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ISO C Compiler 
                                      3 ; Version 4.3.0 #14184 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module main
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _main
                                     12 	.globl _colorSequence
                                     13 	.globl _randomColorSequence
                                     14 	.globl _rand
                                     15 	.globl _NEO_writeColor
                                     16 	.globl _DLY_ms
                                     17 	.globl _PP37
                                     18 	.globl _PP36
                                     19 	.globl _PP35
                                     20 	.globl _PP34
                                     21 	.globl _PP33
                                     22 	.globl _PP32
                                     23 	.globl _PP31
                                     24 	.globl _PP30
                                     25 	.globl _PP17
                                     26 	.globl _PP16
                                     27 	.globl _PP15
                                     28 	.globl _PP14
                                     29 	.globl _PP13
                                     30 	.globl _PP12
                                     31 	.globl _PP11
                                     32 	.globl _PP10
                                     33 	.globl _UIF_BUS_RST
                                     34 	.globl _UIF_DETECT
                                     35 	.globl _UIF_TRANSFER
                                     36 	.globl _UIF_SUSPEND
                                     37 	.globl _UIF_HST_SOF
                                     38 	.globl _UIF_FIFO_OV
                                     39 	.globl _U_SIE_FREE
                                     40 	.globl _U_TOG_OK
                                     41 	.globl _U_IS_NAK
                                     42 	.globl _ADC_CHAN0
                                     43 	.globl _ADC_CHAN1
                                     44 	.globl _CMP_CHAN
                                     45 	.globl _ADC_START
                                     46 	.globl _ADC_IF
                                     47 	.globl _CMP_IF
                                     48 	.globl _CMPO
                                     49 	.globl _U1RI
                                     50 	.globl _U1TI
                                     51 	.globl _U1RB8
                                     52 	.globl _U1TB8
                                     53 	.globl _U1REN
                                     54 	.globl _U1SMOD
                                     55 	.globl _U1SM0
                                     56 	.globl _S0_R_FIFO
                                     57 	.globl _S0_T_FIFO
                                     58 	.globl _S0_FREE
                                     59 	.globl _S0_IF_BYTE
                                     60 	.globl _S0_IF_FIRST
                                     61 	.globl _S0_IF_OV
                                     62 	.globl _S0_FST_ACT
                                     63 	.globl _CP_RL2
                                     64 	.globl _C_T2
                                     65 	.globl _TR2
                                     66 	.globl _EXEN2
                                     67 	.globl _TCLK
                                     68 	.globl _RCLK
                                     69 	.globl _EXF2
                                     70 	.globl _CAP1F
                                     71 	.globl _TF2
                                     72 	.globl _RI
                                     73 	.globl _TI
                                     74 	.globl _RB8
                                     75 	.globl _TB8
                                     76 	.globl _REN
                                     77 	.globl _SM2
                                     78 	.globl _SM1
                                     79 	.globl _SM0
                                     80 	.globl _IT0
                                     81 	.globl _IE0
                                     82 	.globl _IT1
                                     83 	.globl _IE1
                                     84 	.globl _TR0
                                     85 	.globl _TF0
                                     86 	.globl _TR1
                                     87 	.globl _TF1
                                     88 	.globl _RXD
                                     89 	.globl _PWM1_
                                     90 	.globl _TXD
                                     91 	.globl _PWM2_
                                     92 	.globl _AIN3
                                     93 	.globl _VBUS1
                                     94 	.globl _INT0
                                     95 	.globl _TXD1_
                                     96 	.globl _INT1
                                     97 	.globl _T0
                                     98 	.globl _RXD1_
                                     99 	.globl _PWM2
                                    100 	.globl _T1
                                    101 	.globl _UDP
                                    102 	.globl _UDM
                                    103 	.globl _TIN0
                                    104 	.globl _CAP1
                                    105 	.globl _T2
                                    106 	.globl _AIN0
                                    107 	.globl _VBUS2
                                    108 	.globl _TIN1
                                    109 	.globl _CAP2
                                    110 	.globl _T2EX
                                    111 	.globl _RXD_
                                    112 	.globl _TXD_
                                    113 	.globl _AIN1
                                    114 	.globl _UCC1
                                    115 	.globl _TIN2
                                    116 	.globl _SCS
                                    117 	.globl _CAP1_
                                    118 	.globl _T2_
                                    119 	.globl _AIN2
                                    120 	.globl _UCC2
                                    121 	.globl _TIN3
                                    122 	.globl _PWM1
                                    123 	.globl _MOSI
                                    124 	.globl _TIN4
                                    125 	.globl _RXD1
                                    126 	.globl _MISO
                                    127 	.globl _TIN5
                                    128 	.globl _TXD1
                                    129 	.globl _SCK
                                    130 	.globl _IE_SPI0
                                    131 	.globl _IE_TKEY
                                    132 	.globl _IE_USB
                                    133 	.globl _IE_ADC
                                    134 	.globl _IE_UART1
                                    135 	.globl _IE_PWMX
                                    136 	.globl _IE_GPIO
                                    137 	.globl _IE_WDOG
                                    138 	.globl _PX0
                                    139 	.globl _PT0
                                    140 	.globl _PX1
                                    141 	.globl _PT1
                                    142 	.globl _PS
                                    143 	.globl _PT2
                                    144 	.globl _PL_FLAG
                                    145 	.globl _PH_FLAG
                                    146 	.globl _EX0
                                    147 	.globl _ET0
                                    148 	.globl _EX1
                                    149 	.globl _ET1
                                    150 	.globl _ES
                                    151 	.globl _ET2
                                    152 	.globl _E_DIS
                                    153 	.globl _EA
                                    154 	.globl _P
                                    155 	.globl _F1
                                    156 	.globl _OV
                                    157 	.globl _RS0
                                    158 	.globl _RS1
                                    159 	.globl _F0
                                    160 	.globl _AC
                                    161 	.globl _CY
                                    162 	.globl _UEP1_DMA_H
                                    163 	.globl _UEP1_DMA_L
                                    164 	.globl _UEP1_DMA
                                    165 	.globl _UEP0_DMA_H
                                    166 	.globl _UEP0_DMA_L
                                    167 	.globl _UEP0_DMA
                                    168 	.globl _UEP2_3_MOD
                                    169 	.globl _UEP4_1_MOD
                                    170 	.globl _UEP3_DMA_H
                                    171 	.globl _UEP3_DMA_L
                                    172 	.globl _UEP3_DMA
                                    173 	.globl _UEP2_DMA_H
                                    174 	.globl _UEP2_DMA_L
                                    175 	.globl _UEP2_DMA
                                    176 	.globl _USB_DEV_AD
                                    177 	.globl _USB_CTRL
                                    178 	.globl _USB_INT_EN
                                    179 	.globl _UEP4_T_LEN
                                    180 	.globl _UEP4_CTRL
                                    181 	.globl _UEP0_T_LEN
                                    182 	.globl _UEP0_CTRL
                                    183 	.globl _USB_RX_LEN
                                    184 	.globl _USB_MIS_ST
                                    185 	.globl _USB_INT_ST
                                    186 	.globl _USB_INT_FG
                                    187 	.globl _UEP3_T_LEN
                                    188 	.globl _UEP3_CTRL
                                    189 	.globl _UEP2_T_LEN
                                    190 	.globl _UEP2_CTRL
                                    191 	.globl _UEP1_T_LEN
                                    192 	.globl _UEP1_CTRL
                                    193 	.globl _UDEV_CTRL
                                    194 	.globl _USB_C_CTRL
                                    195 	.globl _TKEY_DATH
                                    196 	.globl _TKEY_DATL
                                    197 	.globl _TKEY_DAT
                                    198 	.globl _TKEY_CTRL
                                    199 	.globl _ADC_DATA
                                    200 	.globl _ADC_CFG
                                    201 	.globl _ADC_CTRL
                                    202 	.globl _SBAUD1
                                    203 	.globl _SBUF1
                                    204 	.globl _SCON1
                                    205 	.globl _SPI0_SETUP
                                    206 	.globl _SPI0_CK_SE
                                    207 	.globl _SPI0_CTRL
                                    208 	.globl _SPI0_DATA
                                    209 	.globl _SPI0_STAT
                                    210 	.globl _PWM_CK_SE
                                    211 	.globl _PWM_CTRL
                                    212 	.globl _PWM_DATA1
                                    213 	.globl _PWM_DATA2
                                    214 	.globl _T2CAP1H
                                    215 	.globl _T2CAP1L
                                    216 	.globl _T2CAP1
                                    217 	.globl _TH2
                                    218 	.globl _TL2
                                    219 	.globl _T2COUNT
                                    220 	.globl _RCAP2H
                                    221 	.globl _RCAP2L
                                    222 	.globl _RCAP2
                                    223 	.globl _T2MOD
                                    224 	.globl _T2CON
                                    225 	.globl _SBUF
                                    226 	.globl _SCON
                                    227 	.globl _TH1
                                    228 	.globl _TH0
                                    229 	.globl _TL1
                                    230 	.globl _TL0
                                    231 	.globl _TMOD
                                    232 	.globl _TCON
                                    233 	.globl _XBUS_AUX
                                    234 	.globl _PIN_FUNC
                                    235 	.globl _P3_DIR_PU
                                    236 	.globl _P3_MOD_OC
                                    237 	.globl _P3
                                    238 	.globl _P2
                                    239 	.globl _P1_DIR_PU
                                    240 	.globl _P1_MOD_OC
                                    241 	.globl _P1
                                    242 	.globl _ROM_CTRL
                                    243 	.globl _ROM_DATA_H
                                    244 	.globl _ROM_DATA_L
                                    245 	.globl _ROM_DATA
                                    246 	.globl _ROM_ADDR_H
                                    247 	.globl _ROM_ADDR_L
                                    248 	.globl _ROM_ADDR
                                    249 	.globl _GPIO_IE
                                    250 	.globl _IP_EX
                                    251 	.globl _IE_EX
                                    252 	.globl _IP
                                    253 	.globl _IE
                                    254 	.globl _WDOG_COUNT
                                    255 	.globl _RESET_KEEP
                                    256 	.globl _WAKE_CTRL
                                    257 	.globl _CLOCK_CFG
                                    258 	.globl _PCON
                                    259 	.globl _GLOBAL_CFG
                                    260 	.globl _SAFE_MOD
                                    261 	.globl _DPH
                                    262 	.globl _DPL
                                    263 	.globl _SP
                                    264 	.globl _B
                                    265 	.globl _ACC
                                    266 	.globl _PSW
                                    267 ;--------------------------------------------------------
                                    268 ; special function registers
                                    269 ;--------------------------------------------------------
                                    270 	.area RSEG    (ABS,DATA)
      000000                        271 	.org 0x0000
                           0000D0   272 _PSW	=	0x00d0
                           0000E0   273 _ACC	=	0x00e0
                           0000F0   274 _B	=	0x00f0
                           000081   275 _SP	=	0x0081
                           000082   276 _DPL	=	0x0082
                           000083   277 _DPH	=	0x0083
                           0000A1   278 _SAFE_MOD	=	0x00a1
                           0000B1   279 _GLOBAL_CFG	=	0x00b1
                           000087   280 _PCON	=	0x0087
                           0000B9   281 _CLOCK_CFG	=	0x00b9
                           0000A9   282 _WAKE_CTRL	=	0x00a9
                           0000FE   283 _RESET_KEEP	=	0x00fe
                           0000FF   284 _WDOG_COUNT	=	0x00ff
                           0000A8   285 _IE	=	0x00a8
                           0000B8   286 _IP	=	0x00b8
                           0000E8   287 _IE_EX	=	0x00e8
                           0000E9   288 _IP_EX	=	0x00e9
                           0000C7   289 _GPIO_IE	=	0x00c7
                           008584   290 _ROM_ADDR	=	0x8584
                           000084   291 _ROM_ADDR_L	=	0x0084
                           000085   292 _ROM_ADDR_H	=	0x0085
                           008F8E   293 _ROM_DATA	=	0x8f8e
                           00008E   294 _ROM_DATA_L	=	0x008e
                           00008F   295 _ROM_DATA_H	=	0x008f
                           000086   296 _ROM_CTRL	=	0x0086
                           000090   297 _P1	=	0x0090
                           000092   298 _P1_MOD_OC	=	0x0092
                           000093   299 _P1_DIR_PU	=	0x0093
                           0000A0   300 _P2	=	0x00a0
                           0000B0   301 _P3	=	0x00b0
                           000096   302 _P3_MOD_OC	=	0x0096
                           000097   303 _P3_DIR_PU	=	0x0097
                           0000C6   304 _PIN_FUNC	=	0x00c6
                           0000A2   305 _XBUS_AUX	=	0x00a2
                           000088   306 _TCON	=	0x0088
                           000089   307 _TMOD	=	0x0089
                           00008A   308 _TL0	=	0x008a
                           00008B   309 _TL1	=	0x008b
                           00008C   310 _TH0	=	0x008c
                           00008D   311 _TH1	=	0x008d
                           000098   312 _SCON	=	0x0098
                           000099   313 _SBUF	=	0x0099
                           0000C8   314 _T2CON	=	0x00c8
                           0000C9   315 _T2MOD	=	0x00c9
                           00CBCA   316 _RCAP2	=	0xcbca
                           0000CA   317 _RCAP2L	=	0x00ca
                           0000CB   318 _RCAP2H	=	0x00cb
                           00CDCC   319 _T2COUNT	=	0xcdcc
                           0000CC   320 _TL2	=	0x00cc
                           0000CD   321 _TH2	=	0x00cd
                           00CFCE   322 _T2CAP1	=	0xcfce
                           0000CE   323 _T2CAP1L	=	0x00ce
                           0000CF   324 _T2CAP1H	=	0x00cf
                           00009B   325 _PWM_DATA2	=	0x009b
                           00009C   326 _PWM_DATA1	=	0x009c
                           00009D   327 _PWM_CTRL	=	0x009d
                           00009E   328 _PWM_CK_SE	=	0x009e
                           0000F8   329 _SPI0_STAT	=	0x00f8
                           0000F9   330 _SPI0_DATA	=	0x00f9
                           0000FA   331 _SPI0_CTRL	=	0x00fa
                           0000FB   332 _SPI0_CK_SE	=	0x00fb
                           0000FC   333 _SPI0_SETUP	=	0x00fc
                           0000C0   334 _SCON1	=	0x00c0
                           0000C1   335 _SBUF1	=	0x00c1
                           0000C2   336 _SBAUD1	=	0x00c2
                           000080   337 _ADC_CTRL	=	0x0080
                           00009A   338 _ADC_CFG	=	0x009a
                           00009F   339 _ADC_DATA	=	0x009f
                           0000C3   340 _TKEY_CTRL	=	0x00c3
                           00C5C4   341 _TKEY_DAT	=	0xc5c4
                           0000C4   342 _TKEY_DATL	=	0x00c4
                           0000C5   343 _TKEY_DATH	=	0x00c5
                           000091   344 _USB_C_CTRL	=	0x0091
                           0000D1   345 _UDEV_CTRL	=	0x00d1
                           0000D2   346 _UEP1_CTRL	=	0x00d2
                           0000D3   347 _UEP1_T_LEN	=	0x00d3
                           0000D4   348 _UEP2_CTRL	=	0x00d4
                           0000D5   349 _UEP2_T_LEN	=	0x00d5
                           0000D6   350 _UEP3_CTRL	=	0x00d6
                           0000D7   351 _UEP3_T_LEN	=	0x00d7
                           0000D8   352 _USB_INT_FG	=	0x00d8
                           0000D9   353 _USB_INT_ST	=	0x00d9
                           0000DA   354 _USB_MIS_ST	=	0x00da
                           0000DB   355 _USB_RX_LEN	=	0x00db
                           0000DC   356 _UEP0_CTRL	=	0x00dc
                           0000DD   357 _UEP0_T_LEN	=	0x00dd
                           0000DE   358 _UEP4_CTRL	=	0x00de
                           0000DF   359 _UEP4_T_LEN	=	0x00df
                           0000E1   360 _USB_INT_EN	=	0x00e1
                           0000E2   361 _USB_CTRL	=	0x00e2
                           0000E3   362 _USB_DEV_AD	=	0x00e3
                           00E5E4   363 _UEP2_DMA	=	0xe5e4
                           0000E4   364 _UEP2_DMA_L	=	0x00e4
                           0000E5   365 _UEP2_DMA_H	=	0x00e5
                           00E7E6   366 _UEP3_DMA	=	0xe7e6
                           0000E6   367 _UEP3_DMA_L	=	0x00e6
                           0000E7   368 _UEP3_DMA_H	=	0x00e7
                           0000EA   369 _UEP4_1_MOD	=	0x00ea
                           0000EB   370 _UEP2_3_MOD	=	0x00eb
                           00EDEC   371 _UEP0_DMA	=	0xedec
                           0000EC   372 _UEP0_DMA_L	=	0x00ec
                           0000ED   373 _UEP0_DMA_H	=	0x00ed
                           00EFEE   374 _UEP1_DMA	=	0xefee
                           0000EE   375 _UEP1_DMA_L	=	0x00ee
                           0000EF   376 _UEP1_DMA_H	=	0x00ef
                                    377 ;--------------------------------------------------------
                                    378 ; special function bits
                                    379 ;--------------------------------------------------------
                                    380 	.area RSEG    (ABS,DATA)
      000000                        381 	.org 0x0000
                           0000D7   382 _CY	=	0x00d7
                           0000D6   383 _AC	=	0x00d6
                           0000D5   384 _F0	=	0x00d5
                           0000D4   385 _RS1	=	0x00d4
                           0000D3   386 _RS0	=	0x00d3
                           0000D2   387 _OV	=	0x00d2
                           0000D1   388 _F1	=	0x00d1
                           0000D0   389 _P	=	0x00d0
                           0000AF   390 _EA	=	0x00af
                           0000AE   391 _E_DIS	=	0x00ae
                           0000AD   392 _ET2	=	0x00ad
                           0000AC   393 _ES	=	0x00ac
                           0000AB   394 _ET1	=	0x00ab
                           0000AA   395 _EX1	=	0x00aa
                           0000A9   396 _ET0	=	0x00a9
                           0000A8   397 _EX0	=	0x00a8
                           0000BF   398 _PH_FLAG	=	0x00bf
                           0000BE   399 _PL_FLAG	=	0x00be
                           0000BD   400 _PT2	=	0x00bd
                           0000BC   401 _PS	=	0x00bc
                           0000BB   402 _PT1	=	0x00bb
                           0000BA   403 _PX1	=	0x00ba
                           0000B9   404 _PT0	=	0x00b9
                           0000B8   405 _PX0	=	0x00b8
                           0000EF   406 _IE_WDOG	=	0x00ef
                           0000EE   407 _IE_GPIO	=	0x00ee
                           0000ED   408 _IE_PWMX	=	0x00ed
                           0000EC   409 _IE_UART1	=	0x00ec
                           0000EB   410 _IE_ADC	=	0x00eb
                           0000EA   411 _IE_USB	=	0x00ea
                           0000E9   412 _IE_TKEY	=	0x00e9
                           0000E8   413 _IE_SPI0	=	0x00e8
                           000097   414 _SCK	=	0x0097
                           000097   415 _TXD1	=	0x0097
                           000097   416 _TIN5	=	0x0097
                           000096   417 _MISO	=	0x0096
                           000096   418 _RXD1	=	0x0096
                           000096   419 _TIN4	=	0x0096
                           000095   420 _MOSI	=	0x0095
                           000095   421 _PWM1	=	0x0095
                           000095   422 _TIN3	=	0x0095
                           000095   423 _UCC2	=	0x0095
                           000095   424 _AIN2	=	0x0095
                           000094   425 _T2_	=	0x0094
                           000094   426 _CAP1_	=	0x0094
                           000094   427 _SCS	=	0x0094
                           000094   428 _TIN2	=	0x0094
                           000094   429 _UCC1	=	0x0094
                           000094   430 _AIN1	=	0x0094
                           000093   431 _TXD_	=	0x0093
                           000092   432 _RXD_	=	0x0092
                           000091   433 _T2EX	=	0x0091
                           000091   434 _CAP2	=	0x0091
                           000091   435 _TIN1	=	0x0091
                           000091   436 _VBUS2	=	0x0091
                           000091   437 _AIN0	=	0x0091
                           000090   438 _T2	=	0x0090
                           000090   439 _CAP1	=	0x0090
                           000090   440 _TIN0	=	0x0090
                           0000B7   441 _UDM	=	0x00b7
                           0000B6   442 _UDP	=	0x00b6
                           0000B5   443 _T1	=	0x00b5
                           0000B4   444 _PWM2	=	0x00b4
                           0000B4   445 _RXD1_	=	0x00b4
                           0000B4   446 _T0	=	0x00b4
                           0000B3   447 _INT1	=	0x00b3
                           0000B2   448 _TXD1_	=	0x00b2
                           0000B2   449 _INT0	=	0x00b2
                           0000B2   450 _VBUS1	=	0x00b2
                           0000B2   451 _AIN3	=	0x00b2
                           0000B1   452 _PWM2_	=	0x00b1
                           0000B1   453 _TXD	=	0x00b1
                           0000B0   454 _PWM1_	=	0x00b0
                           0000B0   455 _RXD	=	0x00b0
                           00008F   456 _TF1	=	0x008f
                           00008E   457 _TR1	=	0x008e
                           00008D   458 _TF0	=	0x008d
                           00008C   459 _TR0	=	0x008c
                           00008B   460 _IE1	=	0x008b
                           00008A   461 _IT1	=	0x008a
                           000089   462 _IE0	=	0x0089
                           000088   463 _IT0	=	0x0088
                           00009F   464 _SM0	=	0x009f
                           00009E   465 _SM1	=	0x009e
                           00009D   466 _SM2	=	0x009d
                           00009C   467 _REN	=	0x009c
                           00009B   468 _TB8	=	0x009b
                           00009A   469 _RB8	=	0x009a
                           000099   470 _TI	=	0x0099
                           000098   471 _RI	=	0x0098
                           0000CF   472 _TF2	=	0x00cf
                           0000CF   473 _CAP1F	=	0x00cf
                           0000CE   474 _EXF2	=	0x00ce
                           0000CD   475 _RCLK	=	0x00cd
                           0000CC   476 _TCLK	=	0x00cc
                           0000CB   477 _EXEN2	=	0x00cb
                           0000CA   478 _TR2	=	0x00ca
                           0000C9   479 _C_T2	=	0x00c9
                           0000C8   480 _CP_RL2	=	0x00c8
                           0000FF   481 _S0_FST_ACT	=	0x00ff
                           0000FE   482 _S0_IF_OV	=	0x00fe
                           0000FD   483 _S0_IF_FIRST	=	0x00fd
                           0000FC   484 _S0_IF_BYTE	=	0x00fc
                           0000FB   485 _S0_FREE	=	0x00fb
                           0000FA   486 _S0_T_FIFO	=	0x00fa
                           0000F8   487 _S0_R_FIFO	=	0x00f8
                           0000C7   488 _U1SM0	=	0x00c7
                           0000C5   489 _U1SMOD	=	0x00c5
                           0000C4   490 _U1REN	=	0x00c4
                           0000C3   491 _U1TB8	=	0x00c3
                           0000C2   492 _U1RB8	=	0x00c2
                           0000C1   493 _U1TI	=	0x00c1
                           0000C0   494 _U1RI	=	0x00c0
                           000087   495 _CMPO	=	0x0087
                           000086   496 _CMP_IF	=	0x0086
                           000085   497 _ADC_IF	=	0x0085
                           000084   498 _ADC_START	=	0x0084
                           000083   499 _CMP_CHAN	=	0x0083
                           000081   500 _ADC_CHAN1	=	0x0081
                           000080   501 _ADC_CHAN0	=	0x0080
                           0000DF   502 _U_IS_NAK	=	0x00df
                           0000DE   503 _U_TOG_OK	=	0x00de
                           0000DD   504 _U_SIE_FREE	=	0x00dd
                           0000DC   505 _UIF_FIFO_OV	=	0x00dc
                           0000DB   506 _UIF_HST_SOF	=	0x00db
                           0000DA   507 _UIF_SUSPEND	=	0x00da
                           0000D9   508 _UIF_TRANSFER	=	0x00d9
                           0000D8   509 _UIF_DETECT	=	0x00d8
                           0000D8   510 _UIF_BUS_RST	=	0x00d8
                           000090   511 _PP10	=	0x0090
                           000091   512 _PP11	=	0x0091
                           000092   513 _PP12	=	0x0092
                           000093   514 _PP13	=	0x0093
                           000094   515 _PP14	=	0x0094
                           000095   516 _PP15	=	0x0095
                           000096   517 _PP16	=	0x0096
                           000097   518 _PP17	=	0x0097
                           0000B0   519 _PP30	=	0x00b0
                           0000B1   520 _PP31	=	0x00b1
                           0000B2   521 _PP32	=	0x00b2
                           0000B3   522 _PP33	=	0x00b3
                           0000B4   523 _PP34	=	0x00b4
                           0000B5   524 _PP35	=	0x00b5
                           0000B6   525 _PP36	=	0x00b6
                           0000B7   526 _PP37	=	0x00b7
                                    527 ;--------------------------------------------------------
                                    528 ; overlayable register banks
                                    529 ;--------------------------------------------------------
                                    530 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        531 	.ds 8
                                    532 ;--------------------------------------------------------
                                    533 ; internal ram data
                                    534 ;--------------------------------------------------------
                                    535 	.area DSEG    (DATA)
      000008                        536 _randomColorSequence_green_196608_531:
      000008                        537 	.ds 1
      000009                        538 _randomColorSequence_blue_196608_531:
      000009                        539 	.ds 1
                                    540 ;--------------------------------------------------------
                                    541 ; overlayable items in internal ram
                                    542 ;--------------------------------------------------------
                                    543 ;--------------------------------------------------------
                                    544 ; Stack segment in internal ram
                                    545 ;--------------------------------------------------------
                                    546 	.area SSEG
      000013                        547 __start__stack:
      000013                        548 	.ds	1
                                    549 
                                    550 ;--------------------------------------------------------
                                    551 ; indirectly addressable internal ram data
                                    552 ;--------------------------------------------------------
                                    553 	.area ISEG    (DATA)
                                    554 ;--------------------------------------------------------
                                    555 ; absolute internal ram data
                                    556 ;--------------------------------------------------------
                                    557 	.area IABS    (ABS,DATA)
                                    558 	.area IABS    (ABS,DATA)
                                    559 ;--------------------------------------------------------
                                    560 ; bit data
                                    561 ;--------------------------------------------------------
                                    562 	.area BSEG    (BIT)
                                    563 ;--------------------------------------------------------
                                    564 ; paged external ram data
                                    565 ;--------------------------------------------------------
                                    566 	.area PSEG    (PAG,XDATA)
                                    567 ;--------------------------------------------------------
                                    568 ; uninitialized external ram data
                                    569 ;--------------------------------------------------------
                                    570 	.area XSEG    (XDATA)
                                    571 ;--------------------------------------------------------
                                    572 ; absolute external ram data
                                    573 ;--------------------------------------------------------
                                    574 	.area XABS    (ABS,XDATA)
                                    575 ;--------------------------------------------------------
                                    576 ; initialized external ram data
                                    577 ;--------------------------------------------------------
                                    578 	.area HOME    (CODE)
                                    579 	.area GSINIT0 (CODE)
                                    580 	.area GSINIT1 (CODE)
                                    581 	.area GSINIT2 (CODE)
                                    582 	.area GSINIT3 (CODE)
                                    583 	.area GSINIT4 (CODE)
                                    584 	.area GSINIT5 (CODE)
                                    585 	.area GSINIT  (CODE)
                                    586 	.area GSFINAL (CODE)
                                    587 	.area CSEG    (CODE)
                                    588 ;--------------------------------------------------------
                                    589 ; interrupt vector
                                    590 ;--------------------------------------------------------
                                    591 	.area HOME    (CODE)
      000000                        592 __interrupt_vect:
      000000 02 00 06         [24]  593 	ljmp	__sdcc_gsinit_startup
                                    594 ;--------------------------------------------------------
                                    595 ; global & static initialisations
                                    596 ;--------------------------------------------------------
                                    597 	.area HOME    (CODE)
                                    598 	.area GSINIT  (CODE)
                                    599 	.area GSFINAL (CODE)
                                    600 	.area GSINIT  (CODE)
                                    601 	.globl __sdcc_gsinit_startup
                                    602 	.globl __sdcc_program_startup
                                    603 	.globl __start__stack
                                    604 	.globl __mcs51_genRAMCLEAR
                                    605 	.area GSFINAL (CODE)
      000024 02 00 03         [24]  606 	ljmp	__sdcc_program_startup
                                    607 ;--------------------------------------------------------
                                    608 ; Home
                                    609 ;--------------------------------------------------------
                                    610 	.area HOME    (CODE)
                                    611 	.area HOME    (CODE)
      000003                        612 __sdcc_program_startup:
      000003 02 01 F4         [24]  613 	ljmp	_main
                                    614 ;	return from main will return to caller
                                    615 ;--------------------------------------------------------
                                    616 ; code
                                    617 ;--------------------------------------------------------
                                    618 	.area CSEG    (CODE)
                                    619 ;------------------------------------------------------------
                                    620 ;Allocation info for local variables in function 'randomColorSequence'
                                    621 ;------------------------------------------------------------
                                    622 ;j                         Allocated to registers r6 r7 
                                    623 ;red                       Allocated to registers r4 
                                    624 ;green                     Allocated with name '_randomColorSequence_green_196608_531'
                                    625 ;blue                      Allocated with name '_randomColorSequence_blue_196608_531'
                                    626 ;num                       Allocated to registers r1 
                                    627 ;i                         Allocated to registers r0 r5 
                                    628 ;l                         Allocated to registers r6 r7 
                                    629 ;------------------------------------------------------------
                                    630 ;	main.c:36: void randomColorSequence(void) {
                                    631 ;	-----------------------------------------
                                    632 ;	 function randomColorSequence
                                    633 ;	-----------------------------------------
      000027                        634 _randomColorSequence:
                           000007   635 	ar7 = 0x07
                           000006   636 	ar6 = 0x06
                           000005   637 	ar5 = 0x05
                           000004   638 	ar4 = 0x04
                           000003   639 	ar3 = 0x03
                           000002   640 	ar2 = 0x02
                           000001   641 	ar1 = 0x01
                           000000   642 	ar0 = 0x00
                                    643 ;	main.c:38: for(int j=0;j<NeoPixel;j++){
      000027 7E 00            [12]  644 	mov	r6,#0x00
      000029 7F 00            [12]  645 	mov	r7,#0x00
      00002B                        646 00108$:
      00002B C3               [12]  647 	clr	c
      00002C EE               [12]  648 	mov	a,r6
      00002D 94 10            [12]  649 	subb	a,#0x10
      00002F EF               [12]  650 	mov	a,r7
      000030 64 80            [12]  651 	xrl	a,#0x80
      000032 94 80            [12]  652 	subb	a,#0x80
      000034 40 03            [24]  653 	jc	00142$
      000036 02 00 F0         [24]  654 	ljmp	00102$
      000039                        655 00142$:
                                    656 ;	main.c:39: uint8_t red = rand() % level;
      000039 C0 07            [24]  657 	push	ar7
      00003B C0 06            [24]  658 	push	ar6
      00003D 12 02 F3         [24]  659 	lcall	_rand
      000040 75 11 64         [24]  660 	mov	__modsint_PARM_2,#0x64
      000043 75 12 00         [24]  661 	mov	(__modsint_PARM_2 + 1),#0x00
      000046 12 03 C0         [24]  662 	lcall	__modsint
      000049 AC 82            [24]  663 	mov	r4,dpl
                                    664 ;	main.c:40: uint8_t green = rand() % level;
      00004B C0 04            [24]  665 	push	ar4
      00004D 12 02 F3         [24]  666 	lcall	_rand
      000050 75 11 64         [24]  667 	mov	__modsint_PARM_2,#0x64
      000053 75 12 00         [24]  668 	mov	(__modsint_PARM_2 + 1),#0x00
      000056 12 03 C0         [24]  669 	lcall	__modsint
      000059 AB 82            [24]  670 	mov	r3,dpl
      00005B 8B 08            [24]  671 	mov	_randomColorSequence_green_196608_531,r3
                                    672 ;	main.c:41: uint8_t blue = rand() % level;
      00005D 12 02 F3         [24]  673 	lcall	_rand
      000060 75 11 64         [24]  674 	mov	__modsint_PARM_2,#0x64
      000063 75 12 00         [24]  675 	mov	(__modsint_PARM_2 + 1),#0x00
      000066 12 03 C0         [24]  676 	lcall	__modsint
      000069 AA 82            [24]  677 	mov	r2,dpl
      00006B 8A 09            [24]  678 	mov	_randomColorSequence_blue_196608_531,r2
                                    679 ;	main.c:42: uint8_t num = rand() % NeoPixel;
      00006D 12 02 F3         [24]  680 	lcall	_rand
      000070 75 11 10         [24]  681 	mov	__modsint_PARM_2,#0x10
      000073 75 12 00         [24]  682 	mov	(__modsint_PARM_2 + 1),#0x00
      000076 12 03 C0         [24]  683 	lcall	__modsint
      000079 A9 82            [24]  684 	mov	r1,dpl
      00007B D0 04            [24]  685 	pop	ar4
      00007D D0 06            [24]  686 	pop	ar6
      00007F D0 07            [24]  687 	pop	ar7
                                    688 ;	main.c:44: for(int i=0; i<num; i++){
      000081 78 00            [12]  689 	mov	r0,#0x00
      000083 7D 00            [12]  690 	mov	r5,#0x00
      000085                        691 00105$:
      000085 89 02            [24]  692 	mov	ar2,r1
      000087 7B 00            [12]  693 	mov	r3,#0x00
      000089 C3               [12]  694 	clr	c
      00008A E8               [12]  695 	mov	a,r0
      00008B 9A               [12]  696 	subb	a,r2
      00008C ED               [12]  697 	mov	a,r5
      00008D 64 80            [12]  698 	xrl	a,#0x80
      00008F 8B F0            [24]  699 	mov	b,r3
      000091 63 F0 80         [24]  700 	xrl	b,#0x80
      000094 95 F0            [12]  701 	subb	a,b
      000096 50 2B            [24]  702 	jnc	00101$
                                    703 ;	main.c:45: NEO_writeColor(0, 0, 0);
      000098 75 0A 00         [24]  704 	mov	_NEO_writeColor_PARM_2,#0x00
      00009B 75 0B 00         [24]  705 	mov	_NEO_writeColor_PARM_3,#0x00
      00009E 75 82 00         [24]  706 	mov	dpl,#0x00
      0000A1 C0 07            [24]  707 	push	ar7
      0000A3 C0 06            [24]  708 	push	ar6
      0000A5 C0 05            [24]  709 	push	ar5
      0000A7 C0 04            [24]  710 	push	ar4
      0000A9 C0 01            [24]  711 	push	ar1
      0000AB C0 00            [24]  712 	push	ar0
      0000AD 12 02 3B         [24]  713 	lcall	_NEO_writeColor
      0000B0 D0 00            [24]  714 	pop	ar0
      0000B2 D0 01            [24]  715 	pop	ar1
      0000B4 D0 04            [24]  716 	pop	ar4
      0000B6 D0 05            [24]  717 	pop	ar5
      0000B8 D0 06            [24]  718 	pop	ar6
      0000BA D0 07            [24]  719 	pop	ar7
                                    720 ;	main.c:44: for(int i=0; i<num; i++){
      0000BC 08               [12]  721 	inc	r0
      0000BD B8 00 C5         [24]  722 	cjne	r0,#0x00,00105$
      0000C0 0D               [12]  723 	inc	r5
      0000C1 80 C2            [24]  724 	sjmp	00105$
      0000C3                        725 00101$:
                                    726 ;	main.c:47: NEO_writeColor(red, green, blue);
      0000C3 85 08 0A         [24]  727 	mov	_NEO_writeColor_PARM_2,_randomColorSequence_green_196608_531
      0000C6 85 09 0B         [24]  728 	mov	_NEO_writeColor_PARM_3,_randomColorSequence_blue_196608_531
      0000C9 8C 82            [24]  729 	mov	dpl,r4
      0000CB C0 07            [24]  730 	push	ar7
      0000CD C0 06            [24]  731 	push	ar6
      0000CF 12 02 3B         [24]  732 	lcall	_NEO_writeColor
                                    733 ;	main.c:48: DLY_ms(delay);
      0000D2 90 00 64         [24]  734 	mov	dptr,#0x0064
      0000D5 12 02 CB         [24]  735 	lcall	_DLY_ms
                                    736 ;	main.c:49: NEO_writeColor(0, 0, 0);
      0000D8 75 0A 00         [24]  737 	mov	_NEO_writeColor_PARM_2,#0x00
      0000DB 75 0B 00         [24]  738 	mov	_NEO_writeColor_PARM_3,#0x00
      0000DE 75 82 00         [24]  739 	mov	dpl,#0x00
      0000E1 12 02 3B         [24]  740 	lcall	_NEO_writeColor
      0000E4 D0 06            [24]  741 	pop	ar6
      0000E6 D0 07            [24]  742 	pop	ar7
                                    743 ;	main.c:38: for(int j=0;j<NeoPixel;j++){
      0000E8 0E               [12]  744 	inc	r6
      0000E9 BE 00 01         [24]  745 	cjne	r6,#0x00,00145$
      0000EC 0F               [12]  746 	inc	r7
      0000ED                        747 00145$:
      0000ED 02 00 2B         [24]  748 	ljmp	00108$
      0000F0                        749 00102$:
                                    750 ;	main.c:52: for(int l=0; l<9; l++){
      0000F0 7E 00            [12]  751 	mov	r6,#0x00
      0000F2 7F 00            [12]  752 	mov	r7,#0x00
      0000F4                        753 00111$:
      0000F4 C3               [12]  754 	clr	c
      0000F5 EE               [12]  755 	mov	a,r6
      0000F6 94 09            [12]  756 	subb	a,#0x09
      0000F8 EF               [12]  757 	mov	a,r7
      0000F9 64 80            [12]  758 	xrl	a,#0x80
      0000FB 94 80            [12]  759 	subb	a,#0x80
      0000FD 50 1B            [24]  760 	jnc	00113$
                                    761 ;	main.c:53: NEO_writeColor(0, 0, 0);
      0000FF 75 0A 00         [24]  762 	mov	_NEO_writeColor_PARM_2,#0x00
      000102 75 0B 00         [24]  763 	mov	_NEO_writeColor_PARM_3,#0x00
      000105 75 82 00         [24]  764 	mov	dpl,#0x00
      000108 C0 07            [24]  765 	push	ar7
      00010A C0 06            [24]  766 	push	ar6
      00010C 12 02 3B         [24]  767 	lcall	_NEO_writeColor
      00010F D0 06            [24]  768 	pop	ar6
      000111 D0 07            [24]  769 	pop	ar7
                                    770 ;	main.c:52: for(int l=0; l<9; l++){
      000113 0E               [12]  771 	inc	r6
      000114 BE 00 DD         [24]  772 	cjne	r6,#0x00,00111$
      000117 0F               [12]  773 	inc	r7
      000118 80 DA            [24]  774 	sjmp	00111$
      00011A                        775 00113$:
                                    776 ;	main.c:56: }
      00011A 22               [24]  777 	ret
                                    778 ;------------------------------------------------------------
                                    779 ;Allocation info for local variables in function 'colorSequence'
                                    780 ;------------------------------------------------------------
                                    781 ;j                         Allocated to registers r6 r7 
                                    782 ;red                       Allocated to registers r4 
                                    783 ;green                     Allocated to registers r3 
                                    784 ;blue                      Allocated to registers r2 
                                    785 ;i                         Allocated to registers r1 r5 
                                    786 ;l                         Allocated to registers r4 r5 
                                    787 ;------------------------------------------------------------
                                    788 ;	main.c:58: void colorSequence(void) {
                                    789 ;	-----------------------------------------
                                    790 ;	 function colorSequence
                                    791 ;	-----------------------------------------
      00011B                        792 _colorSequence:
                                    793 ;	main.c:60: for(int j=0;j<=NeoPixel;j++){
      00011B 7E 00            [12]  794 	mov	r6,#0x00
      00011D 7F 00            [12]  795 	mov	r7,#0x00
      00011F                        796 00111$:
      00011F C3               [12]  797 	clr	c
      000120 74 10            [12]  798 	mov	a,#0x10
      000122 9E               [12]  799 	subb	a,r6
      000123 74 80            [12]  800 	mov	a,#(0x00 ^ 0x80)
      000125 8F F0            [24]  801 	mov	b,r7
      000127 63 F0 80         [24]  802 	xrl	b,#0x80
      00012A 95 F0            [12]  803 	subb	a,b
      00012C 50 01            [24]  804 	jnc	00142$
      00012E 22               [24]  805 	ret
      00012F                        806 00142$:
                                    807 ;	main.c:61: uint8_t red = rand() % level;
      00012F C0 07            [24]  808 	push	ar7
      000131 C0 06            [24]  809 	push	ar6
      000133 12 02 F3         [24]  810 	lcall	_rand
      000136 75 11 64         [24]  811 	mov	__modsint_PARM_2,#0x64
      000139 75 12 00         [24]  812 	mov	(__modsint_PARM_2 + 1),#0x00
      00013C 12 03 C0         [24]  813 	lcall	__modsint
      00013F AC 82            [24]  814 	mov	r4,dpl
                                    815 ;	main.c:62: uint8_t green = rand() % level;
      000141 C0 04            [24]  816 	push	ar4
      000143 12 02 F3         [24]  817 	lcall	_rand
      000146 75 11 64         [24]  818 	mov	__modsint_PARM_2,#0x64
      000149 75 12 00         [24]  819 	mov	(__modsint_PARM_2 + 1),#0x00
      00014C 12 03 C0         [24]  820 	lcall	__modsint
      00014F AB 82            [24]  821 	mov	r3,dpl
                                    822 ;	main.c:63: uint8_t blue = rand() % level;
      000151 C0 03            [24]  823 	push	ar3
      000153 12 02 F3         [24]  824 	lcall	_rand
      000156 75 11 64         [24]  825 	mov	__modsint_PARM_2,#0x64
      000159 75 12 00         [24]  826 	mov	(__modsint_PARM_2 + 1),#0x00
      00015C 12 03 C0         [24]  827 	lcall	__modsint
      00015F AA 82            [24]  828 	mov	r2,dpl
      000161 D0 03            [24]  829 	pop	ar3
      000163 D0 04            [24]  830 	pop	ar4
      000165 D0 06            [24]  831 	pop	ar6
      000167 D0 07            [24]  832 	pop	ar7
                                    833 ;	main.c:64: for(int i=0; i<j; i++){
      000169 79 00            [12]  834 	mov	r1,#0x00
      00016B 7D 00            [12]  835 	mov	r5,#0x00
      00016D                        836 00105$:
      00016D C3               [12]  837 	clr	c
      00016E E9               [12]  838 	mov	a,r1
      00016F 9E               [12]  839 	subb	a,r6
      000170 ED               [12]  840 	mov	a,r5
      000171 64 80            [12]  841 	xrl	a,#0x80
      000173 8F F0            [24]  842 	mov	b,r7
      000175 63 F0 80         [24]  843 	xrl	b,#0x80
      000178 95 F0            [12]  844 	subb	a,b
      00017A 50 2C            [24]  845 	jnc	00101$
                                    846 ;	main.c:65: NEO_writeColor(red, green, blue);
      00017C 8B 0A            [24]  847 	mov	_NEO_writeColor_PARM_2,r3
      00017E 8A 0B            [24]  848 	mov	_NEO_writeColor_PARM_3,r2
      000180 8C 82            [24]  849 	mov	dpl,r4
      000182 C0 07            [24]  850 	push	ar7
      000184 C0 06            [24]  851 	push	ar6
      000186 C0 05            [24]  852 	push	ar5
      000188 C0 04            [24]  853 	push	ar4
      00018A C0 03            [24]  854 	push	ar3
      00018C C0 02            [24]  855 	push	ar2
      00018E C0 01            [24]  856 	push	ar1
      000190 12 02 3B         [24]  857 	lcall	_NEO_writeColor
      000193 D0 01            [24]  858 	pop	ar1
      000195 D0 02            [24]  859 	pop	ar2
      000197 D0 03            [24]  860 	pop	ar3
      000199 D0 04            [24]  861 	pop	ar4
      00019B D0 05            [24]  862 	pop	ar5
      00019D D0 06            [24]  863 	pop	ar6
      00019F D0 07            [24]  864 	pop	ar7
                                    865 ;	main.c:64: for(int i=0; i<j; i++){
      0001A1 09               [12]  866 	inc	r1
      0001A2 B9 00 C8         [24]  867 	cjne	r1,#0x00,00105$
      0001A5 0D               [12]  868 	inc	r5
      0001A6 80 C5            [24]  869 	sjmp	00105$
      0001A8                        870 00101$:
                                    871 ;	main.c:67: DLY_ms(delay);
      0001A8 90 00 64         [24]  872 	mov	dptr,#0x0064
      0001AB C0 07            [24]  873 	push	ar7
      0001AD C0 06            [24]  874 	push	ar6
      0001AF 12 02 CB         [24]  875 	lcall	_DLY_ms
      0001B2 D0 06            [24]  876 	pop	ar6
      0001B4 D0 07            [24]  877 	pop	ar7
                                    878 ;	main.c:68: for(int l=0; l<j; l++){
      0001B6 7C 00            [12]  879 	mov	r4,#0x00
      0001B8 7D 00            [12]  880 	mov	r5,#0x00
      0001BA                        881 00108$:
      0001BA C3               [12]  882 	clr	c
      0001BB EC               [12]  883 	mov	a,r4
      0001BC 9E               [12]  884 	subb	a,r6
      0001BD ED               [12]  885 	mov	a,r5
      0001BE 64 80            [12]  886 	xrl	a,#0x80
      0001C0 8F F0            [24]  887 	mov	b,r7
      0001C2 63 F0 80         [24]  888 	xrl	b,#0x80
      0001C5 95 F0            [12]  889 	subb	a,b
      0001C7 50 23            [24]  890 	jnc	00112$
                                    891 ;	main.c:69: NEO_writeColor(0, 0, 0);
      0001C9 75 0A 00         [24]  892 	mov	_NEO_writeColor_PARM_2,#0x00
      0001CC 75 0B 00         [24]  893 	mov	_NEO_writeColor_PARM_3,#0x00
      0001CF 75 82 00         [24]  894 	mov	dpl,#0x00
      0001D2 C0 07            [24]  895 	push	ar7
      0001D4 C0 06            [24]  896 	push	ar6
      0001D6 C0 05            [24]  897 	push	ar5
      0001D8 C0 04            [24]  898 	push	ar4
      0001DA 12 02 3B         [24]  899 	lcall	_NEO_writeColor
      0001DD D0 04            [24]  900 	pop	ar4
      0001DF D0 05            [24]  901 	pop	ar5
      0001E1 D0 06            [24]  902 	pop	ar6
      0001E3 D0 07            [24]  903 	pop	ar7
                                    904 ;	main.c:68: for(int l=0; l<j; l++){
      0001E5 0C               [12]  905 	inc	r4
      0001E6 BC 00 D1         [24]  906 	cjne	r4,#0x00,00108$
      0001E9 0D               [12]  907 	inc	r5
      0001EA 80 CE            [24]  908 	sjmp	00108$
      0001EC                        909 00112$:
                                    910 ;	main.c:60: for(int j=0;j<=NeoPixel;j++){
      0001EC 0E               [12]  911 	inc	r6
      0001ED BE 00 01         [24]  912 	cjne	r6,#0x00,00147$
      0001F0 0F               [12]  913 	inc	r7
      0001F1                        914 00147$:
                                    915 ;	main.c:72: }
      0001F1 02 01 1F         [24]  916 	ljmp	00111$
                                    917 ;------------------------------------------------------------
                                    918 ;Allocation info for local variables in function 'main'
                                    919 ;------------------------------------------------------------
                                    920 ;	main.c:77: void main(void) {
                                    921 ;	-----------------------------------------
                                    922 ;	 function main
                                    923 ;	-----------------------------------------
      0001F4                        924 _main:
                                    925 ;	main.c:78: NEO_init();                       // init NeoPixels
                                    926 ;	assignBit
      0001F4 C2 B3            [12]  927 	clr	_PP33
      0001F6 53 96 F7         [24]  928 	anl	_P3_MOD_OC,#0xf7
      0001F9 43 97 08         [24]  929 	orl	_P3_DIR_PU,#0x08
                                    930 ;	src/system.h:71: SAFE_MOD = 0x55;
      0001FC 75 A1 55         [24]  931 	mov	_SAFE_MOD,#0x55
                                    932 ;	src/system.h:72: SAFE_MOD = 0xAA;                              // enter safe mode
      0001FF 75 A1 AA         [24]  933 	mov	_SAFE_MOD,#0xaa
                                    934 ;	src/system.h:80: __asm__("anl _CLOCK_CFG, #0b11111000");
      000202 53 B9 F8         [24]  935 	anl	_CLOCK_CFG, #0b11111000
                                    936 ;	src/system.h:81: __asm__("orl _CLOCK_CFG, #0b00000101");     // 16MHz	
      000205 43 B9 05         [24]  937 	orl	_CLOCK_CFG, #0b00000101
                                    938 ;	src/system.h:100: SAFE_MOD = 0x00;                              // terminate safe mode
      000208 75 A1 00         [24]  939 	mov	_SAFE_MOD,#0x00
                                    940 ;	main.c:80: DLY_ms(delay);                       // wait for clock to settle
      00020B 90 00 64         [24]  941 	mov	dptr,#0x0064
      00020E 12 02 CB         [24]  942 	lcall	_DLY_ms
                                    943 ;	main.c:83: while (1) {
      000211                        944 00102$:
                                    945 ;	main.c:84: randomColorSequence();
      000211 12 00 27         [24]  946 	lcall	_randomColorSequence
                                    947 ;	main.c:85: DLY_ms(100);
      000214 90 00 64         [24]  948 	mov	dptr,#0x0064
      000217 12 02 CB         [24]  949 	lcall	_DLY_ms
                                    950 ;	main.c:86: colorSequence();
      00021A 12 01 1B         [24]  951 	lcall	_colorSequence
                                    952 ;	main.c:87: DLY_ms(100);
      00021D 90 00 64         [24]  953 	mov	dptr,#0x0064
      000220 12 02 CB         [24]  954 	lcall	_DLY_ms
                                    955 ;	main.c:89: }
      000223 80 EC            [24]  956 	sjmp	00102$
                                    957 	.area CSEG    (CODE)
                                    958 	.area CONST   (CODE)
                                    959 	.area CABS    (ABS,CODE)
