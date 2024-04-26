/** @file CH552-PWM.c (SOURCE)
 *
 *  @brief CH552 PWM example
 *
 *  @author @CesarBautista 
 *
 *  @bug No known bugs.
 */

/******************************************************************************
 * INCLUDES
 *****************************************************************************/

#include <stdio.h>
#include "src/config.h"                   // user configurations
#include "src/system.h"                   // system functions
#include "src/gpio.h"                     // for GPIO
#include "src/delay.h"                    // for delays
#include "src/pwm.h"

/******************************************************************************
 * MACROS AND DEFINES
 *****************************************************************************/

#define MIN_COUNTER 10
#define MAX_COUNTER 254
#define STEP_SIZE   10

/******************************************************************************
 * TYPEDEFS
 *****************************************************************************/

/******************************************************************************
 * PUBLIC FUNCTION PROTOTYPES
 *****************************************************************************/

void change_pwm(int hex_value)
{
    PWM_write(PIN_PWM, hex_value);
}
void main(void) 
{

    CLK_config();                          
    DLY_ms(5);                            
    PWM_set_freq(1);                    
    PIN_output(PIN_PWM);       
    PWM_start(PIN_PWM);      
    PWM_write(PIN_PWM, 0);
while (1) 
{
    for (int i = MIN_COUNTER; i < MAX_COUNTER; i+=STEP_SIZE) 
    {
        change_pwm(i);
        DLY_ms(20);
    }
    for (int i = MAX_COUNTER; i > MIN_COUNTER; i-=STEP_SIZE)
    {
        change_pwm(i);
        DLY_ms(20);
    }
    
}
}
