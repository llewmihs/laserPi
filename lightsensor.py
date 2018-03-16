#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os
from gpiozero import LED

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

#start up - get average light reading with and without LED
# laser.off()
# total=0
# for i in range(5):
#     total = total + RCtime(18)
#     time.sleep(0.2)
# avDark = total/5
# print("Average dark reading is %d" % avDark)

while True:
    #turn of the LED
    #laser.off()
    print(RCtime(18))     # Read RC timing using pin #18
    #get average light level

