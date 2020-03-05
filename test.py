#!/usr/bin/env python3
# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


ts2 = TouchSensor(INPUT_2)
ts3 = TouchSensor(INPUT_3)

leds = Leds()

print("Press left to turn green, right to turn red")

while True:
    if t2.is_pressed:
      leds.set_color("LEFT", "GREEN")
      leds.set_color("RIGHT", "RED")
    if t3.is_pressed:
      leds.set_color("LEFT", "RED")
      leds.set_color("RIGHT", "GREEN")
