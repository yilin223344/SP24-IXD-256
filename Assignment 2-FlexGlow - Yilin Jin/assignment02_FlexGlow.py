import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import math

title0 = None
label0 = None
label1 = None
label2 = None
label3 = None

adc1 = None
pin41 = None
rgb2 = None
my_count = 0
update_timer = 0
motion_timer = 0
program_state = 'IDLE'

imu_x_val = 0.0   
imu_y_val = 0.0   
imu_y_last = 0.0  

def setup():
  global title0, label0, label1, label2, label3, adc1, pin41
  global rgb2
  global my_count
  M5.begin()
  rgb2 = RGB(io=7, n=30, type="SK6812")
  rgb2.fill_color(0x000000)
  # initialize title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("assignment2", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  
  # initialize labels ("label text", x, y, layer number, fg color, bg color, font): 
  label0 = Widgets.Label("--", 3, 30, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label1 = Widgets.Label("--", 3, 50, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label2 = Widgets.Label("--", 3, 70, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label3 = Widgets.Label("--", 4, 90, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  
  adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)
  
  pin41 = Pin(41, mode=Pin.IN)

def map_value(in_val, in_min, in_max, out_min, out_max):
  out_val = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if out_val < out_min:
    out_val = out_min
  elif out_val > out_max:
    out_val = out_max
  return int(out_val)

def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

# function to combine hue, saturation, brightness into one color value:
def hsb_to_color(h, s, v):
    h = float(h)/255.0
    s = float(s)/255.0
    v = float(v)/255.0
    
    i = math.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]
    r = int(255 * r)
    g = int(255 * g)
    b = int(255 * b)
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color

def loop():
  global label0, label1, label2, label3, adc1
  global update_timer, motion_timer, program_state
  global adc1_val, imu_x_val, imu_y_val, imu_y_last
  global rgb2
  global my_count
  M5.update()
  
  # read ADC value:
  adc1_val = adc1.read()
  
  # read button value:
  button_value = pin41.value()
  
  # map the ADC value from 0-4095 to 0-255 range:
  adc1_val_8bit = map_value(adc1_val, 0, 4095, 0, 255)
  
  # read the IMU accelerometer values:
  imu_val = Imu.getAccel()
  
  imu_x_val = imu_val[0]  # update X-axis acceleration value
  imu_x_val_8bit = map_value(imu_y_val, -1.0, 1.0, 0, 255)
  
  imu_y_last = imu_y_val  # save the last imu_y_val
  imu_y_val = imu_val[1]  # update Y-axis acceleration value
  # map IMU Y-axis acceleration from 0.0 - 1.0 to 0 - 255 range:
  imu_y_val_8bit = map_value(imu_y_val, 0.0, 1.0, 0, 255)

  # Y-axis acceleration difference (absolute value):
  imu_y_diff = imu_y_val - imu_y_last
  
  #print(imu_y_diff)
  time.sleep_ms(300)
  if program_state == 'IDLE':
    # change from IDLE to MOTION state when motion is detected:
    if imu_y_diff > 0.15 or imu_y_diff < -0.15:
      program_state = 'MOTION'
      motion_timer = time.ticks_ms()
      # reset motion timer:
      print('my_cont', my_count)
      #print(program_state)
      if my_count == 5:
        for i in range(5):  # loop from 0 - 5
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
        #my_count = 0  # reset my_count
      elif my_count == 10:
        for i in range(5, 10): 
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
      elif my_count == 15:
        for i in range(10, 15):  
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
      elif my_count == 20:
        for i in range(15, 20):  
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
      elif my_count == 25:
        for i in range(20, 25):  
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
      elif my_count == 30:
        for i in range(25, 30):  
          color = hsb_to_color(i, 255, 255)
          rgb2.set_color(i, color) 
        time.sleep_ms(1000)
        
  
        
  elif program_state == 'MOTION':
    if(time.ticks_ms() > motion_timer + 500):
      program_state = 'IDLE'
      my_count = my_count +1

  if time.ticks_ms() > update_timer + 100:
    # update update_timer with current time in milliseconds:
    update_timer = time.ticks_ms()
    
    red = get_color(adc1_val_8bit, 0, 0)
    green = get_color(0, imu_x_val_8bit, 0)
    blue = get_color(0, 0, imu_y_val_8bit)
  
    label0.setText('ADC: ' + str(adc1_val))
    label0.setColor(0xffffff, red)
    
    # show IMU X-axis acceleration with 0.2 precision on display label1:
    imu_x_str = 'IMU X: {:0.2f}'.format(imu_x_val)
    label1.setText(imu_x_str)
    label1.setColor(0xffffff, green)
    
    # show IMU X-axis acceleration with 0.2 precision on display label2:
    imu_y_str = 'IMU Y: {:0.2f}'.format(imu_y_val)
    label2.setText(imu_y_str)
    label2.setColor(0xffffff, blue)
    
    label3.setText(program_state)


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