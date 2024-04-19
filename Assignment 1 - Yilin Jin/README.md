# Assignment 1：Key holder

## Introduction
My first project is a “key holder” with four different states in it. The inspiration for this project was that I often lose my keys because I don't have a special place to keep them. This project can remind me that when I get home, the first thing is to put the key in the holder, the led light and display are obvious, and will not be easy to forget.

When the key is not in the box, the screen will display "I'm hungry :o" on a white background, the RGB light’s color is white. This means to remind the user to put the key in.

When the key is placed in the box, the metal on the key will touch the copper tape on the box. At this time, the screen will change to a purple background shows “Thank you :)", and the RGB light’s color will change from white to purple. This means the key is in the holder.

## Design Sketches
![idea 2](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/d18aff4c-0bec-464a-83c7-cb089e2580ca)

## State diagram
![+ Flowchart](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/042d2dfb-5071-46a8-898a-a1b5b51dae69)

## Firmware

Input LED lights color and the patterns for the screen
``` Python
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
```
``` Python
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
```

## States
### State 1
![state1](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/996963f3-c38f-4dda-85d4-9480bec0248c)
### State 2
![state2](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/b5f5b20b-0406-4e70-95b5-39cef45f1d7e)
