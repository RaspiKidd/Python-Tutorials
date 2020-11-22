# LED Matrix

## Objective

Learn how to use the LED matrix on the micro:bit which can be used as a screen to output data.

We are going to explore how to use the LED matrix with Python.

 ---
 **NOTE:** You will need to a micro:bit to complete this tutorial.

---

## Starting Python

1. Open your favourite web browser(we recommend Google Chrome)
2. Within the address bar type [python.microbit.org](https://python.microbit.org/v/2.0)

## Pairing your micro:bit
1. Click on Connect
2. Click on your micro:bit and click connect.

## Code Snippets

These are the pieces of code that we can use to control the LED matrix.

1. `display.scroll("Hello World")` This does exactly what it says and scrolls text on the LED matrix.

2. `display.scroll(0)` This does exactly as it says and scrolls a number on the LED matrix.

3. `display.scroll(Image.HAPPY)` This allows us to display preconfigured images on the LED matrix.

4. `display.set_Pixel(0,0,5)` This lights up one of the LEDs on the matrix by taking a value for the row, column and brightness you want the LED

5. `display.off()` This displays an arrow or compass direction on the LED matrix

6. `image = Image("00500:""00000:""50505:""00000:""00500")` This allows you to create your own images by changing the 0's(off) to 5's(on).

## Displaying Text

1. Type `while True:` and press enter. This will create a loop that will last forever or until you switch your micro:bit off.

2. Type `display.scroll("Hello World")`. This will make Hello World scroll across the LED matrix.

3. Click on Flash to download and run the code on your micro:bit.

Your code should look like this:

```python
from microbit import *

while True:
  display.scroll("Hello World")
```

## Displaying Numbers

1. Type `while True:` and press enter. This will create a loop that lasts forever or until you switch your micro:bit off.

2. Type `display.scroll(7)`. This will make the number 7 display on the LED matrix.

3. Click on Flash to download and run the code on your micro:bit.

Your code should look like this:

```python
from microbit import *

while True:
  display.scroll(7)
```

## Display Image

1. Type `while True:` and press enter. This will create a loop that lasts for ever or until you switch your micro:bit off.

2. Type `display.show(Image.DUCK)`. This will display a duck on the LED matrix.

3. Click on Flash to download and run the code on your micro:bit.

Your code should look like this:

```python
from microbit import *

while True:
  display.show(Image.DUCK)
```

## Set Pixel

1. Type `while True:` and press enter. This will create a loop that lasts forever or until you switch your micro:bit off.

2. Type `display.set_pixel(2,2,5)` This will make the middle LED light up on the display.

3. Click on Flash to download and run your code on your micro:bit.

Your Code should look like this:

```python
from microbit import *

while True:
  display.set_pixel(2,2,5)
```

## Create Image

1. Type `image = Image("00500:""00000:""50505:""00000:""00500")` and press enter. This will create a variable called "image".

2. Type `while True:` and press enter. This will create a loop that will last for ever or until you switch your micro:bit off.

3. Type `display.show(image)`. This will display the image variable we created earlier.

4. Click on Flash to download and run the code on your micro:bit.

Your code should look like this:

```python
from microbit import *

image = Image("00500:""00000:""50505:""00000:""00500")

while True:
  display.show(image)
```

## Turn the Display Off

We are going to re-purpose our code from above and add to it for this next bit of code.

1. Type `sleep(5000)` and press enter.  This will pause our program for 5 seconds.

2. Type `display.off()`. This will turn the LED matrix off.

4. Click on Flash to download and run the code on your micro:bit.

Your code should look like this:

```python
from microbit import *

image = Image("00500:""00000:""50505:""00000:""00500")

while True:
  display.show(image)
  sleep(5000)
  display.off()
```

## Conclusion

We have now learned how to use the LED matrix on the micro:bit

> ## Challenge
>
> You now know how to use all the display code snippets on their own.
>
> Why not try and use a few of them together to create your own program.
