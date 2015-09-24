import RPi.GPIO as GPIO
from time import sleep
from functools import partial
from random import randint
import lights_config as config

GPIO.setmode(GPIO.BCM)

def createLight(pin):
  GPIO.setup(pin, GPIO.OUT)
  return partial(GPIO.output, pin)


lightRow = [
  createLight(config.blue),
  createLight(config.green),
  createLight(config.yellow),
  createLight(config.red)
]

def clean ():
  for light in lightRow:
    light(0)

def iterLight (lights):
  for light in lights:
    light(1)
    sleep(0.3)
    light(0)

def createLightToggle (light):
    state = [True]
    def toggle ():
      light(int(state[0]))
      state[0] = not state[0]

    return toggle

def blink_all():
  for light in lightRow:
    light(1)
  sleep(0.3)
  for light in lightRow:
    light(0)
  sleep(0.3)

def blink_any():
  light = lightRow[randint(0, len(lightRow)-1)]
  light(1)
  sleep(0.3)
  light(0)
  sleep(0.3)



def toggle (lights) :
  for lightToggle in lights:
    lightToggle()
    sleep(0.3)


menu = [
    partial(iterLight, lightRow),
    partial(iterLight, lightRow + lightRow[-2:-len(lightRow):-1]),
    partial(toggle, map(createLightToggle, lightRow + lightRow[::-1])),
    blink_all,
    blink_any
]
try:
  while True:
    clean()
    print ("Blinking Menu")
    print ("*************")
    print ("1 Cycle")
    print ("2 Ping Pong")
    print ("3 Cumulating")
    print ("4 Blink all")
    print ("5 Blink Random")
    option = raw_input ("Please select an option: ")
    try:
      while True:
        menu[int(option) - 1]()
    except IndexError:
      print ("Invalid option")
    except KeyboardInterrupt:
      pass

except KeyboardInterrupt:
  GPIO.cleanup()
