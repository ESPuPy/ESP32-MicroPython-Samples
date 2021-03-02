#
# list3  
# sample program for ADC
#
from machine import Pin
from machine import ADC
import utime

# Available Pins: 32-39
adc = ADC(Pin(36))
adc.read()

adc.atten(ADC.ATTN_11DB)   # maximum input voltage of approximately 3.6v
adc.width(ADC.WIDTH_10BIT) # 0-1023
print(adc.read())
while True:
    print(adc.read())
    utime.sleep_ms(100)
