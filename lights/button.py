import RPi.GPIO as GPIO
import lights_config as config

GPIO.setmode(GPIO.BCM)

GPIO.setup(config.button, GPIO.IN)

def trackChange(init):
  value = [init]
  def changed(newValue):
    if (newValue == value[0]):
      return False
    value[0] = newValue
    return True

  return changed

btnState = trackChange(GPIO.input(config.button))

try:
  while True:
    state = GPIO.input(config.button)
    change = btnState(state)
    if change == True:
      if state == True:
        print("Button pressed")
      else:
        print("Button released")
except KeyboardInterrupt:
  GPIO.cleanup()
