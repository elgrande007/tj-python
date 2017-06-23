#!/usr/bin/env python

"""
Author: Brian McGinnis and Patrick McGinnis

Notes: The Servo is acting up a bit. May need to change to another library.
Need to suppress the warnings that the GPIO library is giving for a cleaner GUI
It warns that the Channel is already in use because it has been serup before.

5 has it in upright position 10 is down

"""

import RPi.GPIO as GPIO
import time



def map( x,  in_min,  in_max,  out_min,  out_max):
  return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)



class Servo:
        pwm = None

        def __init__(self):

                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(26, GPIO.OUT)
                self.pwm=GPIO.PWM(26,50)
                
                
        def wave(self, times):
                self.armUp()
                while (times > 0):
                        self.armDown()
                        self.armUp()
                        times = times - 1
                self.pwm.stop()
        
        def angle(self, degrees):
                #degrees MUST BE between 0 and 180
                self.pwm.start(map(degrees, 0, 180, 1, 15))
                time.sleep(1)
                self.pwm.stop()

        def armUp(self):
                self.angle(15)
                
        def armDown(self):
                self.angle(15)
                
#s = servo()
#s.wave(2)
#s.armDown()
#s.armUp()
