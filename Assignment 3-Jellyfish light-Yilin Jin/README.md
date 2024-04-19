# Assignment 1：Key holder

## Introduction
![project description](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/6fa5a98e-d644-4bc0-a909-0bdc7b051ef3)

## Design Sketches
![sketch1](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/f280017a-5d3f-43c9-bb8c-9da4036a4891)

## State diagram 
<img width="993" alt=" state diagram " src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/58527dd8-0fd3-4d99-8c7d-5b5914788fae">

## Firmware
The light sensor controls color and rotation
``` Python
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
```
## Final outcome
### Standby State
![Standby State](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/cca26794-d271-4c92-8eb5-5c244364292b)

### Handhold State
![Handhold State](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/6587847c-428d-4526-bb51-31878b20b716)
