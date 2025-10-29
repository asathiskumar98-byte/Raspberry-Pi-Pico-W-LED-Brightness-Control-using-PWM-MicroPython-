from machine import Pin, PWM
from time import sleep

led = machine.Pin(17,machine.Pin.OUT)  #LED

pwm  = machine.PWM(led)

pwm.freq(5000)  # Freq PWM = 5000Hz

while True:
    pwm.duty_u16(65535)  # 0 = 0% 65535 = 100%