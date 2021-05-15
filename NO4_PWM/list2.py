#
# list2
#
import utime
from machine import Pin
from machine import ADC
from machine import PWM

PWM_FREQ = 100 # freq of PWM 100Hz
PWM_MIN_DUTY = 0
PWM_MAX_DUTY = 1023

#Pins 32-39

# setup ADC              # set GPIO36 as ADC
adc = ADC(Pin(36))       # connect thr VR to GPIO36

# maximum voltate applied to AD convertr : 3.6v
adc.atten(ADC.ATTN_11DB)

# set data range to 0-1023
adc.width(ADC.WIDTH_10BIT)

# set GPIO AND PWM
pwm_led = PWM(Pin(25)) # LED port GPIO:25
pwm_led.freq(PWM_FREQ)

while True:
    vol = adc.read()
    # Get the voltage from the VR (0 =< vol <= 1023)
    duty = int(PWM_MAX_DUTY * vol / 1023)
    # Calculate the duty cycle according to the voltage
    pwm_led.duty(duty)      # set duty cycle in PWM
    print("vol:{:d} duty:{:d}".format(vol,duty))
    utime.sleep_ms(100)     # wait 100ms
    
