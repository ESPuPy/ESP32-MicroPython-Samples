#
# list5
# notice:
#  to execute this sample, encder.py is required
#
from machine import Pin
from machine import PWM
import utime
import encoder

A4 = 440

# setup RotaryEncoder
enc = encoder.RotaryEncoder(Pin(39, Pin.IN), Pin(34, Pin.IN))

# set GPIO AND PWM
pwm_sound = PWM(Pin(26))
pwm_sound.duty(int(1024/2))

freq = A4
pwm_sound.freq(freq)

while True:
    val = enc.get_val()
    if val:
        print(val)
        if val == 1:
            freq += 5
        else:
            freq -= 5
        print("{:d}Hz".format(freq))
        pwm_sound.freq(freq)

