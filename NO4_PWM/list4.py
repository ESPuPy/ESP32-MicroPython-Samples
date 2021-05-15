#
# list4
#
from machine import Pin
from machine import PWM
import utime

# set GPIO AND PWM
pwm_sound = PWM(Pin(26))
pwm_sound.duty(int(1024/2))

G3=196
A3=220
B3=246
C4=262
D4=294
E4=330
F4=349
G4=392
A4=440
B4=494
C5=523

#CHIME1=(C5, B4, A4, G4, F4, E4, D4, C4, B3, A3, G3)
CHIME1=(C5, B4, A4, G4, F4, E4, D4, C4)

while True:
    for freq in CHIME1:
        pwm_sound.freq(freq)
        print(freq)
        utime.sleep_ms(180)

pwm_sound.duty(0) # to stop sound


