#! /usr/bin python

# Using a button to light an LED

# AUTHOR: Kerry Kidd		VERSION: 2		DATE: 09/03/15

# import libraries
import os			# Gives python access to Linux commands
import time			# Provides time related commands
import RPi.GPIO as GPIO		# Gives python access to the GPIO pins

GPIO.setmode(GPIO.BCM) 		#Set the GPIO pin naming mode
GPIO.setwarnings(False) 	#Supress warnings

# Setting up variables
Button = 25
Led = 18

# Setting up pin 25 as an input and pin 18 as an output
GPIO.setup (Button,GPIO.IN)
GPIO.setup (Led, GPIO.OUT)


print "------------------" # Printng to screen
print " Button + GPIO " # Printing to screen
print "------------------" # Printing to screen

GPIO.output (Led, True) # Turning the LED off
while 1:
	if GPIO.input(Button): # Checking whether the button has been pressed
		GPIO.output(Led, False) # Turning the LED on if button is pressed
	else: # Button has not been pressed
		GPIO.output (Led, True) # Led off

GPIO.cleanup () # Setting GPIO pins back to default
