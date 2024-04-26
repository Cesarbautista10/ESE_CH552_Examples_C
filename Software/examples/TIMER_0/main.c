
#include <stdio.h>
#include "src/config.h"                   // user configurations
#include "src/system.h"                   // system functions
#include "src/gpio.h"                     // for GPIO
#include "src/delay.h"                    // for delays
#include "src/pwm.h"


volatile uint16_t counter;



// once timer triggers this interrupt, we'll set the TL and TH values, so 
// it will start to increment from there
// The formula used to calculate TL and TH values in regards to the 16 bit `counter`:
// Timer0/1 will _always_ increment TL/TH every 12th clock cycle:
// max_val_of_counter+1 * ((0xffff-0xTHTL) * (1/(FREQ_SYS/12)) = seconds for the counter to overflow
// our `counter` is 16 bit, so the max value is 0xffff:
// (0xffff+1)*(0xffff-0xffe0)*(1/(24000000/12)) = 1.015 seconds

//     // we will update this `counter` on every interrupt

void timer0_interrupt(void) __interrupt(INT_NO_TMR0)	/* Timer0 interrupt service routine (ISR) */
{
    PIN_toggle(PIN_BUZZER);
    TH0 = 0xFF;      	/* 50ms timer value */
    TL0 = 0x00;      
}

int main(void)
{
    CLK_config();  
    DLY_ms(5);
    PIN_output(PIN_BUZZER);
	EA  = 1;         	/* Enable global interrupt */
	ET0 = 1;         	/* Enable timer0 interrupt */
	
	TH0 = 0xFF;		/* 50ms timer value */
	TL0 = 0x00;      
    TMOD = 0x01;		/* Timer0 mode1 */
	TR0 = 1;  	      	/* Start timer0 */
  	while(1);
}