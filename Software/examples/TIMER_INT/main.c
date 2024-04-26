

#include <stdio.h>
#include "src/config.h"                   // user configurations
#include "src/system.h"                   // system functions
#include "src/gpio.h"                     // for GPIO
#include "src/delay.h"                    // for delays


#define I2C_DELAY_H()

volatile uint8_t buffer = 0;
volatile uint8_t current_state = 0;
volatile uint8_t data = 0;
volatile uint8_t config = 0;
volatile uint8_t command =0;
volatile uint8_t count = 0;
volatile uint8_t flag = 0;
volatile unsigned int timeout_counter = 0;


#define PIN_INT P32
volatile uint16_t counter;


void ext0_interrupt(void) __interrupt(INT_NO_INT0)
{
    PIN_toggle(PIN_LED);  
}

int main(void)
{
    CLK_config();  
    DLY_ms(5);
    PIN_output_OD(PIN_INT);  
    PIN_output(PIN_LED);
    
	EA  = 1;     /* Enable global interrupt */
    EX0 = 1;    // Enable INT0
    IT0 = 1;    // INT0 is edge triggered

    while(1)
    {
        // Do nothing
    }
    
}