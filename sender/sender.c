#include <util/delay.h>
#include <stdio.h>
#include <stdint.h>
#include <avr/io.h>
#include "uart.c"

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
	UART_init();
	
	uint8_t buf[50];
   
	DDRB |= mask;
  	int i = 0;
  	char sent = 0;
	while(1) {
 
	  	while((UCSR0A & (1<<RXC0))) {
	  		uint8_t c = (uint8_t) UART_getChar();
	  		buf[i] = c;
	  		i++;
	  	}
	  	
	  	if (i == 7) {
		  	for (int j=0; j<i; j++) {
	  			UART_putChar((uint8_t)buf[j]);
	  		}
	  		UART_putChar((uint8_t)27);
  		}
	}
}
