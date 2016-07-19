#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def led1_init():
 GPIO.setup(LED1, GPIO.OUT)

def led1_on():
 GPIO.output(LED1, GPIO.HIGH)

def led1_off():
 GPIO.output(LED1, GPIO.LOW)

def led2_init():
 GPIO.setup(LED2, GPIO.OUT)

def led2_on():
 GPIO.output(LED2, GPIO.HIGH)

def led2_off():
 GPIO.output(LED2, GPIO.LOW)

def led3_init():
 GPIO.setup(LED3, GPIO.OUT)

def led3_on():
 GPIO.output(LED3, GPIO.HIGH)

def led3_off():
 GPIO.output(LED3, GPIO.LOW)


GPIO.setmode(GPIO.BCM)

LED1 = 6
led1_init()

LED2 = 5
led2_init()

LED3 = 11
led3_init()

for i in range(10):
 print(i)
 led1_on()
 time.sleep(0.1)

 led2_on()
 time.sleep(0.1)

 led3_on()
 time.sleep(0.1)

 led1_off()
 time.sleep(0.1)

 led2_off()
 time.sleep(0.1)

 led3_off()
 time.sleep(0.1)

GPIO.cleanup()
