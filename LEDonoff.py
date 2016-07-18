#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED1 = 5	
GPIO.setup(LED1, GPIO.OUT)


for i in range(20):
 print(i)
 GPIO.output(LED1, GPIO.HIGH)
 time.sleep(0.1)
 GPIO.output(LED1, GPIO.LOW)
 time.sleep(0.1)

GPIO.cleanup()

print("led1 done")
