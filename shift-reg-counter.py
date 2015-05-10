#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pinDS   = 22
pinSTCP = 27
pinSHCP = 17
pinLED  = 23

def pinSetup():
    """Initialize the GPIO pins once before using them."""
    GPIO.setmode(GPIO.BCM)
    for i in [ pinDS, pinSTCP, pinSHCP, pinLED ]:
        print "Setting up %d" % i
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)

def shiftNumber(number):
    """Shift in the bits needed to drive an 8 segment display to show
       number passed in on it."""
    displaySeg = [
      [ False, False, True, True, True, True, True, True, ],      # 0
      [ False, False, False, False, False, True, True, False, ],  # 1
      [ False, True, False, True, True, False, True, True, ],     # 2
      [ False, True, False, False, True, True, True, True, ],     # 3
      [ False, True, True, False, False, True, True, False, ],    # 4
      [ False, True, True, False, True, True, False, True, ],     # 5
      [ False, True, True, True, True, True, False, True, ],      # 6
      [ False, False, False, False, False, True, True, True, ],   # 7
      [ False, True, True, True, True, True, True, True, ],       # 8
      [ False, True, True, False, True, True, True, True, ],      # 9
    ]

    for z in range(8):
        GPIO.output(pinSHCP, False)
        GPIO.output(pinDS, displaySeg[number][z])
        GPIO.output(pinSHCP, True)
        GPIO.output(pinDS, False)
        GPIO.output(pinSHCP, False)
    return True

def latch():
    """Drive the STCP/latch pin to update output pins."""
    GPIO.output(pinLED, True)
    GPIO.output(pinSTCP, True)
    GPIO.output(pinSTCP, False)
    GPIO.output(pinLED, False)

def countNumbers():
    """Count from 00 to 99 and display on two 74hc595 shift registers
       in serial."""
    for i in range(10):
        for j in range(10):
            shiftNumber(j) # Ones digit
            shiftNumber(i) # Tens digit
            print "Sending number %d%d" % (i, j)
            latch()
            time.sleep(0.1)

try:    
    if __name__ == '__main__':
        pinSetup()
        while True:
            countNumbers()
except KeyboardInterrupt:
   GPIO.cleanup()
