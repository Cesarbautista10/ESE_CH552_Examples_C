#include "src/system.h" 
#include "src/gpio.h"   
#include "src/delay.h"  

#define PIN_ADC P11

void main(void)
{
  CLK_config();
  DLY_ms(5);

  ADC_input(PIN_ADC);

  ADC_enable();

  while (1)
  {
    int data = ADC_read(); // read ADC value 0 - 255 (8-bit)
  }
}