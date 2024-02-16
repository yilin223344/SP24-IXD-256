import os, sys, io
import M5
from M5 import *
from hardware import *
import time

pin_label = None
program_state_label = None

input_pin = None
input_value = 0
input_timer = 0
rgb2 = None
label1 = None

program_state = 'START'

def setup():
  global pin_label, program_state_label, input_pin
  global rgb2
  global label1
  M5.begin()
  pin_label = Widgets.Label("input", 5, 5, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  program_state_label = Widgets.Label("START", 5, 25, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  input_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)

def loop():
  global pin_label, program_state_label
  global input_value
  global input_timer
  global program_state
  global rgb2
  global label1
  M5.update()
  if time.ticks_ms() > input_timer + 500:
    input_timer = time.ticks_ms()
    input_value = input_pin.value()
    if input_value == 0:
      Widgets.fillScreen(0xd052ed)
      label1 = Widgets.Label("Thank you :)", 7, 54, 1.0, 0xffffff, 0xd052ed, Widgets.FONTS.DejaVu18)
      rgb2 = RGB(io=2, n=10, type="SK6812")
      rgb2.fill_color(0xcc33cc)
    else:
      Widgets.fillScreen(0xffffff)
      label1 = Widgets.Label("I'm hungry:o", 7, 54, 1.0, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
      rgb2 = RGB(io=2, n=10, type="SK6812")
      rgb2.fill_color(0xffffff)
  if program_state == 'START':
    if input_value == 0:
      program_state = 'RUN'  
      
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

