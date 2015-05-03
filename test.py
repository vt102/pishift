#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin   = 23

def pinSetup():
    GPIO.setmode(GPIO.BCM)
    for i in [ pin ]:
        print "Setting up %d" % i
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)

def countNumbers():
    while True:
        GPIO.output(pin, True)
        time.sleep(0.5)
        GPIO.output(pin, False)
        time.sleep(0.5)


try:    
    if __name__ == '__main__':
        pinSetup()
        countNumbers()
except KeyboardInterrupt:
   GPIO.cleanup()
