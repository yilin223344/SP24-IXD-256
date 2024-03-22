import os, sys, io
import M5
from M5 import *
from unit import LightUnit
from hardware import *
from servo import Servo
servo = None
uart0 = None
light_0 = None
mylight = None
rgb2 = None

def setup():
  global uart0, light_0, mylight
  global servo
  global rgb2
  light_0 = LightUnit((1,2))
  M5.begin()
  servo = Servo(pin=38)
  # stop the servo:
  servo.move(90) 
  rgb2 = RGB(io=5, n=10, type="SK6812")
  rgb2.fill_color(0x33ccff)


def loop():
  global uart0, light_0, mylight
  M5.update()
  mylight = light_0.get_analog_value()
  print(mylight)
  if 58000 < mylight:
    servo.move(80)
    rgb2 = RGB(io=5, n=10, type="SK6812")
    rgb2.fill_color(0x33ccff)
  else:
    servo.move(90)
    rgb2 = RGB(io=5, n=10, type="SK6812")
    rgb2.fill_color(0x000000)


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")