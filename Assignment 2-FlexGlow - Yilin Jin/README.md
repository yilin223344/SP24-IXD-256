# Assignment 2：FlexGlow

## Introduction
![project description](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/b5a88b6f-df59-43ed-926c-293c3926193c)

## State diagram
<img width="1067" alt="state diagram" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/3c2b7eb5-4966-4b84-846c-2eea0aa16f44">

## Firmware
Sets the range of values
``` Python
  def map_value(in_val, in_min, in_max, out_min, out_max):
  out_val = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if out_val < out_min:
    out_val = out_min
  elif out_val > out_max:
    out_val = out_max
  return int(out_val)
```
Gradient rainbow colors
``` Python
  def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

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
```
Set the color change and time for each group
``` Python
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
```
## Project outcome

![final photo](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/5dd6608f-36e0-46d7-821d-d4a08f076508)

<img width="858" alt="final photo 2" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/a8aea2c1-47df-4ae2-8028-6ab422548920">
