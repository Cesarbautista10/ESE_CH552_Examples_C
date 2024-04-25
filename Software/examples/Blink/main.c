
#include "src/system.h" 
#include "src/gpio.h"  
#include "src/delay.h"  

#define PIN_LED P34

void main(void)
{
  CLK_config();
  DLY_ms(5);

  PIN_output(PIN_LED);
  while (1)
  {
    // Toggle LED state every 500ms
    PIN_toggle(PIN_LED);
    DLY_ms(500);
  }
}