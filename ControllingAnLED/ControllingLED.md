# Controlling an LED

Within this tutorial you are going to learn how to create a simple circuit and using the Raspberry Pi and Python to control an LED.

## What You Will Need

The equipment you need is;

* 1 x LED
* 2 x Male to Female jumper wires
* 1 x breadboard
* A Raspberry Pi

## Creating The Circuit

Let's create the electronic circuit that we are going to control using Python and a Raspberry Pi.

The Circuit will look like this:

![LED Circuit](Images/LEDCircuit.png) ![GPIO pin out](Images/PinOut.png)

**NOTE:** The LED has one short leg known as the cathode (Negative = -) and one long leg known as the anode (positive = +)

The Anode is connected to pin 18 on the Raspberry Pi
The Cathode is connected to ground on the Raspberry Pi

Once the LED is wired to the Raspberry Pi this completes our electronic circuit.

We can now code our LED to do something.

## Coding The LED

### Turning The LED On

1. Open up your favourite Python Editor. I will be using Mu through this tutorial as it is a beginner friendly editor.

2.  