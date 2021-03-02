#
#  list2  
#  LED Toggle Sample (Interrupt Handler)
#
from  machine import Pin
import utime

led_sw_on = False   # LED toggle flag
last_switch_time = 0
CHATTER_MASK = 300  # ignore interrupt in 300msec

# interrupt handler
def sw_handler(sw):
    global led_sw_on
    global last_switch_time
    current_ms = utime.ticks_ms()
    if utime.ticks_diff(current_ms, last_switch_time) < CHATTER_MASK:
        pass
    else:
        led_sw_on = not led_sw_on
        last_switch_time = current_ms

sw = Pin(33, Pin.IN, Pin.PULL_UP)
sw.irq(handler=sw_handler, trigger=Pin.IRQ_FALLING)

led = Pin(25, Pin.OUT)
led.off()

# main loop
while True:
    if led_sw_on:
        print("LED on")   # for debug
        led.on()          # LED ON
    else:
        print("LED off")  # for debug
        led.off()         # LED OFF
    utime.sleep_ms(500)
