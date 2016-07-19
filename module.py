#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def led1_init():
 GPIO.setup(LED1, GPIO.OUT)


def led1_on():
 GPIO.output(LED1, GPIO.HIGH)

def led1_off():
 GPIO.output(LED1, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

LED1 = 5
led1_init()

for i in range(10):
 print(i)
 led1_on()
 time.sleep(0.1)

 led1_off()
 time.sleep(0.1)

GPIO.cleanup()
