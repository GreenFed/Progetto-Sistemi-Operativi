#include <util/delay.h>
#include <stdio.h>
#include <stdint.h>
#include <avr/io.h>
#include "../avr_common/uart.h" // this includes the printf and initializes it

const uint8_t mask=(1<<6);

void send_one() {
    for (long i = 0; i < 2048 * 0.01; i++ ) 
	{
   		// 1 / 2048  = 488uS, or 244uS high and 244uS low to create 50% duty cycle
		PORTB = mask;
		_delay_ms(0.244);
		PORTB = 0;
		_delay_ms(0.244);
	}
}

void send_zero() {
	_delay_ms(1);
}

int main(void){

  printf_init();
  
  uint16_t buf[62];
  
  for (int i = 0; i < 63; i++) {
  	buf[i] = 65280;
  }
   
  DDRB |= mask;
  
  while(1) {
  	for (int i = 0; i < 63; i++) {
  		for (int k=16; k>0; k--) {
  			int mask1 = 1 << k;
  			if ( (buf[i] & mask1) == 0 ) {
  				send_zero();
  			} else {
  				send_one();
  			}
  			_delay_ms(100);
  		}
  	}
  }
}
