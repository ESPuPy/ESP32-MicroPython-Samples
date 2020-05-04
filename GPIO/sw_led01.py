#-----------------------------------------
#  GPIO Sample
#  list1 / SW and LED test
#-----------------------------------------
from machine import Pin
import utime
sw = Pin(33, Pin.IN, Pin.PULL_UP)     # enable GPIO33 pullup
led = Pin(25, Pin.OUT)                # set GPIO25 as OUTPUT
while True:
    if  sw.value() == 0:               # SW is pushed  (value: 0)
        print("on")                    # print for debug
        led.on()                       # turn on LED
    else:                              # SW is no pushed (value:1)
        print("off")                   # print for debug
        led.off()                      # turn off LED
    utime.sleep_ms(50)                 # wait for 50msec
#---------------------------------------------------
