import RPi.GPIO as GPIO
import time
import lights_config as config

GPIO.setmode(GPIO.BCM)

GPIO.setup(config.red, GPIO.OUT)
GPIO.output(config.red, 1)
time.sleep(1)

GPIO.output(config.red, 0)
GPIO.cleanup()
