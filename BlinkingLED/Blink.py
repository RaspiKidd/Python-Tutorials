#! /usr/bin python

# Making the three LED's blink

# AUTHOR: Kerry Kidd		VERSION: 1		DATE: 09/03/15

# Import libraries

import time 			# A collection of time related commands
import RPi.GPIO as GPIO		# The GPIO commands

# Setting the GPIO pins naming mode
GPIO.setmode (GPIO.BCM)

# Telling python not to print GPIO warnings on screen
GPIO.setwarnings (False)

# Set pins 18, 23 and 24 to be outputs
GPIO.setup (18, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (24, GPIO.OUT)

# Turn LED's ON
GPIO.output (18, GPIO.HIGH)
GPIO.output (23, GPIO.HIGH)
GPIO.output (24, GPIO.HIGH)

# Pause for 1 second
time.sleep (1)

# Turn LED's OFF
GPIO.output (18, GPIO.LOW)
GPIO.output (23, GPIO.LOW)
GPIO.output (24, GPIO.LOW)

# Pause for 1 second
time.sleep (1)

# Turn LED's ON
GPIO.output (18, GPIO.HIGH)
GPIO.output (23, GPIO.HIGH)
GPIO.output (24, GPIO.HIGH)

# Pause for 1 second
time.sleep (1)

# Turn LED's OFF
GPIO.output (18, GPIO.LOW)
GPIO.output (23, GPIO.LOW)
GPIO.output (24, GPIO.LOW)

# Set the GPIO pins back to default
GPIO.cleanup ()



