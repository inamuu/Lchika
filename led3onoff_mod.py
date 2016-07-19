#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def led_init(leds):
 GPIO.setup(leds, GPIO.OUT)

def led_on(leds):
 GPIO.output(leds, GPIO.HIGH)

def led_off(leds):
 GPIO.output(leds, GPIO.LOW)

LED1 = 6
led_init(LED1)

LED2 = 5
led_init(LED2)

LED3 = 11
led_init(LED3)

for i in range(10):
 print(i)
 led_on(LED1)
 led_on(LED2)
 led_on(LED3)
 time.sleep(0.5)

 led_off(LED1)
 led_off(LED2)
 led_off(LED3)
 time.sleep(0.5)

GPIO.cleanup()

