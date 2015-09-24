import RPi.GPIO as GPIO
from time import sleep
from functools import partial
import lights_config as config

GPIO.setmode(GPIO.BCM)

GPIO.setup(config.button, GPIO.IN)

def createLight(pin):
  GPIO.setup(pin, GPIO.OUT)
  return partial(GPIO.output, pin)

def trackChange(init):
  value = [init]
  def changed(newValue):
    if (newValue == value[0]):
      return False
    value[0] = newValue
    return True

  return changed

def blink(light, time):
  while (time > 0):
    light(1)
    sleep(0.3)
    light(0)
    sleep(0.3)
    time -= 0.6

btnState = trackChange(GPIO.input(config.button))
red = createLight(config.red)
yellow = createLight(config.yellow)
green = createLight(config.green)
blue = createLight(config.blue)

green(1)

try:
  while True:
    state = GPIO.input(config.button)
    change = btnState(state)
    if change == True:
      if state == True:
        green(0)
        yellow(1)
        sleep(0.6)
        yellow(0)
        red(1)
        blink(blue, 6)
        yellow(1)
        sleep(0.6)
        red(0)
        yellow(0)
        green(1)
      else:
        green(1)
except KeyboardInterrupt:
  GPIO.cleanup()
