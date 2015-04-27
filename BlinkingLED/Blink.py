#! /usr/bin python

# Making an LED blink

# AUTHOR: Kerry Kidd		VERSION: 1		DATE: 09/03/15

# Import libraries

import time 			# A collection of time related commands
import RPi.GPIO as GPIO		# The GPIO commands

# Setting the GPIO pins naming mode
GPIO.setmode (GPIO.BCM)

# Telling python not to print GPIO warnings on screen
GPIO.setwarnings (False)

# Set pins 18 to be an output
GPIO.setup (18, GPIO.OUT)

# Turn LED ON
GPIO.output (18, GPIO.HIGH)


# Pause for 1 second
time.sleep (1)

# Turn LED OFF
GPIO.output (18, GPIO.LOW)

# Pause for 1 second
time.sleep (1)

# Turn LED ON
GPIO.output (18, GPIO.HIGH)

# Pause for 1 second
time.sleep (1)

# Turn LED OFF
GPIO.output (18, GPIO.LOW)

# Set the GPIO pins back to default
GPIO.cleanup ()
