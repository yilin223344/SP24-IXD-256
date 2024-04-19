# Final Project: Pure Sphere

## Introduction
There is very little time to contact nature nowadays. Hugs and Natural remedies such as consuming chamomile, lavender, and omega-3, these help relieve anxiety symptoms.

My idea was to create an installation that could help people in their busy lives be at home by embracing this transparent ball. Give feedback to the experiencer and reduce their stress by simulating the natural environment and the feeling of hugging.

Therefore, through the pressure sensor, raindrops and natural sounds on the display can be controlled. The LEG light on the ball device will also change.

## Design Sketches
![Stress relief](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/a72dea09-deae-4f59-90c1-2ff28b653c55)

## Implementation
### Hardware
· 1 Atom s3 board
· 1 pressure sensor
· 1 LED string

### State diagram
<img width="1189" alt="state diagram" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/d1a48a46-eeb2-4223-991c-934bc7601c3c">

## Firmware
After getting the mechanical components ready, I started writing firmware and the screen rain dynamic interaction.

Pressure sensor setup
``` Python
adc = ADC(Pin(PRESSURE_SENSOR_PIN))
adc.atten(ADC.ATTN_11DB)
```
Define the range of values received by the sensor
``` Python
  # map the ADC value from 0-4095 to 0-255 range:
  adc1_val_8bit = map_value(adc1_val, 0, 4095, 0, 255)
```
LED string control brightness according to pressure
``` Python
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color
```
``` Python
brightness = 255 - adc1_val_8bit
  r = int(brightness * 235/255)  
  g = int(brightness * 225/255)  
  b = int(brightness * 52/255)  
  rgb_color = get_color(r, g, b)
  rgb.fill_color(rgb_color)
```

The screen displays raindrops and falls controlled by a pressure sensor
``` Python
from pyodide.ffi import create_proxy
      from main import *

      p5.setup = create_proxy(setup)
      p5.draw = create_proxy(draw)
      setup()
```
Control location and how many raindrops fall
``` Python
if(sensor_val < 50):
    if p5.random(1) < p5.map(sensor_val, 0, 255, 0.05, 0.2): 
      createDrop(p5.random(1512), 0) 

  
  if len(drops) != 0:
    for drop in drops:
      fall(drop)  
      display(drop)  
      updateTrail(drop)  
```
``` Python
def createDrop(x, y):
    drop = {'x': x, 'y': y, 'speed': p5.random(1, 5), 'trail': [], 'trailLength': 20}
    drops.append(drop)

def fall(drop):
    drop['y'] += drop['speed']  
    if drop['y'] > 982:  
        index = drops.index(drop)  
        if index != -1:
            drops.pop(index)  

def display(drop):
    if drop:
        p5.push()
        p5.noStroke()  
        p5.fill(1, 57, 71)  
        p5.ellipse(drop['x'], drop['y'], 10, 10)  
        p5.pop()
```
``` Python
def updateTrail(drop):
    if drop:
        drop['trail'].append(p5.createVector(drop['x'], drop['y']))

        if len(drop['trail']) > drop['trailLength']:
            drop['trail'].pop(0)

        
        for i in range(len(drop['trail'])):
            transparency = p5.map(i, 0, len(drop['trail']), 0, 255)
            p5.push()
            p5.fill(1, 57, 71, transparency)  
            p5.noStroke()
            p5.ellipse(drop['trail'][i].x, drop['trail'][i].y, 10, 10)
            p5.pop()
```

The sound changes according to the sensor and another bird sound is added after 5 seconds of pressing.
``` Python
sound1 = p5.loadSound('soft_rain.mp3') 
sound2 = p5.loadSound('birds.mp3')
sound_timer = 0
```
``` Python
if(sound_state == 'NO SOUND'):
    if(sensor_val < 100):
      #print('play sound 1')
      sound1.play()
      sound_state = 'SOUND 1'
      # update sound timer:
      sound_timer = p5.millis()  
  elif(sound_state == 'SOUND 1'):
    if(p5.millis() > sound_timer + 5000):
      #print('5 seconds passed..')
      sound2.play()
      sound_state = 'SOUND 2'

  if(sound_state == 'SOUND 1') or (sound_state == 'SOUND 2'):
    if(sensor_val > 100):
      #print('stop sounds')
      sound1.stop()
      sound2.stop()
      sound_state = 'NO SOUND'
```
## Integrations
I used p5.js code to control the raindrop and status on the screen. So it allows direct feedback from the sensor and gets dynamic feedback to control the rain.

<img width="257" alt="Screenshot 2024-04-18 at 1 25 21 PM" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/92298213-a50d-4893-8137-67979deef16c">

![WechatIMG479](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/3e8ee211-ae0a-4e48-b58d-60a258c908ee)


## Enclosure Design
The pressure sensor controls the pressure by conducting different numerical control interactions.

![sensor](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/22d5ba00-8328-4d17-af41-6908d509ce76)

The Atom s3 board detects pressure and transmits the led strip and screen.

![Implementation2](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/4428e13c-647b-405f-a097-3d902071fd9d)

The sphere is made of PVC transparent material, which better blends into the natural background and reduces the interaction barrier. The base is made of wood material and natural jute thread, which is more environmentally friendly and natural.

![Implementation3](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/f751d96b-7fae-47d6-bf17-d5c5995631e3)

![Implementation1](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/171208c2-0ae2-47b8-a810-39b8d5cb7789)

## Project outcome
[Prototype link](https://youtu.be/TjiBvIwxByI)

![IMG_8937](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/9cf18c84-97f3-4ab8-83f6-522d406c794d)
![IMG_8938](https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/c9fbedfd-1388-4ecd-9d72-24fe07cd637d)


## Conclusion
Concluding this project and this term, I learned a lot about coding through MicroPython. How to use the code on the device, how to build the enclosure, how to debug the details of the code, etc. These are the challenges encountered and what I learned in the production process.

I tried the code and screen interaction of p5.js for the first time in this final assignment. The emphasis was placed on interaction with people and how to reduce stress by simulating the natural environment through the device. Transparent spheres minimize interaction barriers. Each interaction has its meaning, and the interaction of hugs and brightness is also a relaxing experience. The switching of sound and the feedback of screen interaction provide an immersive experience environment. Providing an environment where you can relax at any time is the goal of this project.

Overall, this course allowed me to achieve the installation I wanted to do. I enjoyed the process from the sketch to the final outcome. In the future, I will continue to use the knowledge learned to design more interactive installation art.




