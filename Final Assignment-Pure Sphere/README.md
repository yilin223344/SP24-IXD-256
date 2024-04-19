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
      p5.mousePressed = create_proxy(mousePressed)
```
``` Python
<div class="contain">
        <div id="data" style="position: absolute; left: 10px; top: 40px;">
            100</div>


        <div style="position: absolute; z-index: 1; left: 10px; top: 10px;">
          <button id="connect-button" type="button">🔌 Connect</button>
          <!--<input type="range" min="0" max="1024" value="100" id="slider">-->
        </div>

        <script>
          const connectButton = document.getElementById ('connect-button');

          let reader;
          let readableStreamClosed;
          let writer;
          let writableStreamClosed;
```
``` Python
async function getReader() {
              port = await navigator.serial.requestPort({});
              await port.open({ baudRate: 115200 });
              console.log(port);
              console.log(port.getInfo());
              connectButton.innerText = '🔌 Disconnect';
              const textDecoder = new TextDecoderStream();
              readableStreamClosed = port.readable.pipeTo(textDecoder.writable);
              reader = textDecoder.readable
                  .pipeThrough(new TransformStream(new LineBreakTransformer()))
                  .getReader();

              while (true) {
                  const { value, done } = await reader.read();
                  if (done) {
                      reader.releaseLock();
                      break;
                  }
                  if (value) {
                      console.log('received.. ' + value);
                      const textElement = document.getElementById("data");
                      textElement.textContent = value;
```
``` Python
let port;
          if ('serial' in navigator) {
              connectButton.addEventListener('click', async function () {
                  if (port) {

                      try {
                          reader.cancel().catch(error => console.log(error));
                          await readableStreamClosed.catch(() => {});
                      } catch (error) {
                          console.log(error);
                      } finally {
                          await port.close();
                          console.log('close port..');
                          port = undefined;
                          connectButton.innerText = '🔌 Connect';
                      }
                  }
                  else {
                      getReader();
```

The sound changes according to the sensor and another bird sound is added after 5 seconds of pressing.
``` Python

```
## Integrations
I used p5.js code to control the raindrop and status on the screen. So it allows direct feedback from the sensor and gets dynamic feedback to control the rain.

<img width="257" alt="Screenshot 2024-04-18 at 1 25 21 PM" src="https://github.com/yilin223344/Yilin-SP24-IXD-256/assets/125238982/92298213-a50d-4893-8137-67979deef16c">

## Enclosure Design



## Project outcome
[Prototype link](https://youtu.be/TjiBvIwxByI)

## Conclusion
Concluding this project and this term, I learned a lot about coding through MicroPython. How to use the code on the device, how to build the enclosure, how to debug the details of the code, etc. These are the challenges encountered in the production process.

I tried the code and screen interaction of p5.js in this final assignment. The emphasis was placed on interaction with people and how to reduce stress by simulating the natural environment through the device. Transparent spheres minimize interaction barriers. Each interaction has its meaning, and the interaction of hugs and brightness is also a relaxing experience. The switching of sound and the feedback of screen interaction provide an immersive experience environment. Providing an environment where you can relax at any time is the goal of this project.

Overall, this course allowed me to achieve the installation I wanted to do. I enjoyed the process from the sketch to the final outcome. In the future, I will continue to use the knowledge learned to design more interactive installation art.




