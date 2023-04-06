import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
pwm=gpio.PWM(2, 50)

pwm.start(0)
    
try:
    while (True):
        a=int(input())
        pwm.start(a)
        print("{:.2f}".format(a*3.3/100))

finally:
    pwm.stop()
    gpio.output(2, 0)
    gpio.cleanup()