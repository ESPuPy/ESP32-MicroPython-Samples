#
#  list5.py
#  sample program for Rotary Encoder
#
from machine import Pin
import encoder
enc = encoder.RotaryEncoder(Pin(39,Pin.IN),Pin(34,Pin.IN))
while True:
    val = enc.get_val()
    if val:
        print(val)
