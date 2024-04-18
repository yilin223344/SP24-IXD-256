# Assignment 1：Key holder

## Introduction
My first project is a “key holder” with four different states in it. The inspiration for this project was that I often lose my keys because I don't have a special place to keep them. This project can remind me that when I get home, the first thing is to put the key in the holder, the led light and display are obvious, and will not be easy to forget.

When the key is not in the box, the screen will display "I'm hungry :o" on a white background, the RGB light’s color is white. This means to remind the user to put the key in.

When the key is placed in the box, the metal on the key will touch the copper tape on the box. At this time, the screen will change to a purple background showing “Thank you :)", and the RGB light’s color will change from white to purple. This means the key is in the holder.
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




