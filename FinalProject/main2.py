import js as p5
from js import document

data_string = None
data_list = None

sound_state = 'NO SOUND'

button_val = None
button_state = 'UP'

sensor_val = 0

# load image data and assign it to variable:
swirl_img = p5.loadImage('swirl.png')

forest_img = p5.loadImage('forest.png')

# load font data and assign it to variable:
jellee_font = p5.loadFont('Jellee.otf')

# load sound data and assign it to variable:
#sound = p5.loadSound('shoot.wav') 
sound1 = p5.loadSound('soft_rain.mp3') 
sound2 = p5.loadSound('shoot.wav')

sound_timer = 0

def setup():
  #p5.createCanvas(1920, 1080)
  p5.createCanvas(1512, 982)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

def draw():
  p5.background(255)
  global data_string, data_list
  global sound_state, button_val
  global sensor_val
  global button_state
  global sound_timer

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  sensor_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  #button_val = int(data_list[1])

  p5.fill(0)
  p5.text('sensor_val =' + str(sensor_val), 10, 20)

  p5.noStroke()  # disable stroke
  # fill function can take 1 argument (gray)
  p5.fill(0)  # black fill
  
  image_x = p5.width/2
  image_y = p5.height/2
  image_w = 300
  image_h = 200
  p5.image(forest_img, image_x, image_y, image_w, image_h)

  p5.fill(0)

  if(sound_state == 'NO SOUND'):
    if(sensor_val < 100):
      print('play sound 1')
      sound1.play()
      sound_state = 'SOUND 1'
      # update sound timer:
      sound_timer = p5.millis()  
  elif(sound_state == 'SOUND 1'):
    if(p5.millis() > sound_timer + 5000):
      print('5 seconds passed..')
      sound2.play()
      sound_state = 'SOUND 2'

  if(sound_state == 'SOUND 1') or (sound_state == 'SOUND 2'):
    if(sensor_val > 100):
      print('stop sounds')
      sound1.stop()
      sound2.stop()
      sound_state = 'NO SOUND'


  # state 1, rain sound
  # if(sound_state = 1):
  #   p5.text('play sound..', 20, 20)
  # else if(sound_state = 2):
  #   #state 2, other sound
  #   p5.text('stop sound rain..', 20, 20)
  #   p5.text('play sound other..', 20, 20)


def mousePressed(event):
  #print('mouse pressed!')
  pass # do nothing
