#
# list1
#
import utime
import math
from machine import Pin
from machine import PWM

PWM_FREQ = 100 # freq of PWM 100Hz

#    0: LED off (0%)
# 512 : duty    (50%)
# 1023: LED ON  (100%)
PWM_MIN_DUTY = 0    # minimum of duty cycle
PWM_MAX_DUTY = 1023 # maximum of duty cycle

# set GPIO AND PWM
pwm_led = PWM(Pin(25)) # set GPIO25 to PWM output

# set freq of PWM
pwm_led.freq(PWM_FREQ)

while True:
    for x in range(100): # make brigt
        pwm_led.duty(int(math.sin(3.14 / 2 * x / 100) * PWM_MAX_DUTY))
        utime.sleep_ms(3)
    utime.sleep_ms(800)
    for x in range(100): # make dim
        pwm_led.duty(int(math.sin(3.14 / 2 * x / 100 + 3.14 / 2) * PWM_MAX_DUTY))
        utime.sleep_ms(10)
    utime.sleep_ms(250)
