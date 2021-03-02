#
# list1
#
from machine import Pin
import utime

sw = Pin(33, Pin.IN, Pin.PULL_UP) # enable pull up of GPIO33

led = Pin(25, Pin.OUT)   # set GPIO25 as OUTPUT
while True:
    if sw.value() == 0:  # if SW is pressed (value:0)
        print("on")      # printing for debug
        led.on()         # LED on
    else:                # if SW is not pressed (value:1)
        print("off")     # printing for debug
        led.off()        # LED OFF
    utime.sleep_ms(50)   # wait for 50ms
