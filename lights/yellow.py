import RPi.GPIO as GPIO
import time
import lights_config as config

GPIO.setmode(GPIO.BCM)

GPIO.setup(config.yellow, GPIO.OUT)
GPIO.output(config.yellow, 1)
time.sleep(1)

GPIO.output(config.yellow, 0)
GPIO.cleanup()
