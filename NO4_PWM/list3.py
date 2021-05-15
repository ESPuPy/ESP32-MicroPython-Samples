#
# list3
#
import utime
from machine import Pin
from machine import ADC
from machine import PWM

PWM_MIN_DUTY = 0
PWM_MAX_DUTY = 1023
PWM_SERVO_FREQ = 50  # freq of PWM 50Hz 20ms
SERVO_DUTY_MIN = 30  # = PWM_MAX_DUTY * 0.5msec / 20msec + safety margin(4)
SERVO_DUTY_MAX = 120 # = PWM_MAX_DUTY * 2.4msec / 20msec - safety margin(3)
SERVO_DUTY_CENTER = int((SERVO_DUTY_MAX - SERVO_DUTY_MIN)/2) + SERVO_DUTY_MIN

# setup Volume input via ADC
adc = ADC(Pin(36)) # VR input GPIO:36
adc.atten(ADC.ATTN_11DB)

# maximum input voltage of approximately 3.6v
adc.width(ADC.WIDTH_10BIT) # 0-1023
VOL_MAX=1023

# set GPIO AND PWM for Servo
pwm_servo = PWM(Pin(17)) # Servo port GPIO:17
pwm_servo.freq(PWM_SERVO_FREQ)
pwm_servo.duty(SERVO_DUTY_CENTER)
while True:
    vol = adc.read()
    duty = int((SERVO_DUTY_MAX - SERVO_DUTY_MIN) * vol / VOL_MAX) + SERVO_DUTY_MIN
    pwm_servo.duty(duty)

    # for debug
    pulse = 1000 / PWM_SERVO_FREQ * duty / 1023
    print("vol:{:d} duty:{:d}({:.2f}ms)".format(vol,duty, pulse))

