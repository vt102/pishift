#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pinDS   = 22
pinSTCP = 27
pinSHCP = 17
pinLED  = 23

displaySeg = [
  [ False, False, True, True, True, True, True, True, ],  # 0
  [ False, False, False, False, False, True, True, False, ],  # 1
  [ False, True, False, True, True, False, True, True, ],  # 2
  [ False, True, False, False, True, True, True, True, ],  # 3
  [ False, True, True, False, False, True, True, False, ],  # 4
  [ False, True, True, False, True, True, False, True, ],  # 5
  [ False, True, True, True, True, True, False, True, ],  # 6
  [ False, False, False, False, False, True, True, True, ],  # 7
  [ False, True, True, True, True, True, True, True, ],  # 8
  [ False, True, True, False, True, True, True, True, ],  # 9
]


def pinSetup():
    GPIO.setmode(GPIO.BCM)
    for i in [ pinDS, pinSTCP, pinSHCP, pinLED ]:
        print "Setting up %d" % i
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)

def countNumbers():
    for i in range(10):
        for j in range(10):
            for z in range(8):
                GPIO.output(pinSHCP, False)
                GPIO.output(pinDS, displaySeg[j][z])
                GPIO.output(pinSHCP, True)
                GPIO.output(pinDS, False)
                GPIO.output(pinSHCP, False)
            for z in range(8): 
                GPIO.output(pinSHCP, False)
                GPIO.output(pinDS, displaySeg[i][z])
                GPIO.output(pinSHCP, True)
                GPIO.output(pinDS, False)
                GPIO.output(pinSHCP, False)
            print "Sending number %d%d" % (i, j)
            GPIO.output(pinLED, True)
            GPIO.output(pinSTCP, True)
            time.sleep(0.5)
            GPIO.output(pinSTCP, False)
            GPIO.output(pinLED, False)
            time.sleep(0.1)

try:    
    if __name__ == '__main__':
        pinSetup()
        while True:
            countNumbers()
except KeyboardInterrupt:
   GPIO.cleanup()
