#! usr/bin python
# Turning an LED on and off again

# Importing the raspberry pi GPIO library as GPIO
import RPi.GPIO as GPIO

# Importing the time library for timing functions
import time

# Setting the naming convetion for the GPIO pins
GPIO.setmode (GPIO.BCM)

# Telling python not to print GPIO warning messages to the screen
GPIO.setwarnings (False)

# Setup pin 18 as an output
GPIO.setup (18, GPIO.OUT)

# Turning The LED on
print "Light On"
GPIO.output (18, GPIO.HIGH)

# Pause for 5 seconds
time.sleep (5)

# Turning the LED off
print "Light Off"
GPIO.output (18, GPIO.LOW)

# Pause for 5 seconds
time.sleep (5)

# Set GPIO pins back to default
GPIO.cleanup()
