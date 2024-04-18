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

## Firmware
After getting the mechanical components ready, I started writing firmware and the screen rain dynamic interaction.

Pressure sensor setup
``` Python
adc = ADC(Pin(PRESSURE_SENSOR_PIN))
adc.atten(ADC.ATTN_11DB)
```
Define the range of values received by the sensor
``` Python

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

```
The sound changes according to the sensor and another bird sound is added after 5 seconds of pressing.
``` Python

```
## Integrations
I used p5.js code to control the raindrop and status on the screen. So it allows direct feedback from the sensor and gets dynamic feedback to control the rain.

<img width="257" alt="Screenshot 2024-04-18 at 1 25 21 PM" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/92298213-a50d-4893-8137-67979deef16c">

## Enclosure Design



## Project outcome

## Conclusion




