import RPi.GPIO as GPIO
import time

inPin = 8
led = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    value = GPIO.input(inPin)
    print (value)
    if value:
        print("Pressed")
        GPIO.output(led,GPIO.HIGH)
    else:
        print("Not Pressed")
        GPIO.output(led,GPIO.LOW)
    time.sleep(0.1)
GPIO.cleanup()