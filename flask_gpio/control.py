import RPi.GPIO as GPIO
def turn_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
def turn_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
