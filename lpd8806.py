from bibliopixel.led import *
from bibliopixel.animation import BaseStripAnim
from bibliopixel.drivers.LPD8806 import *
from math import *

class StripTest(BaseStripAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(StripTest, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
        #Fill the strip, with each sucessive color
	cycle = math.floor(self._step / 300) % 3
	if cycle == 1: 
            for i in range(self._led.numLEDs):
               self._led.set(i, self._colors[(self._step + i) % len(self._colors)])
            #Increment the internal step by the given amount
	if cycle == 0: 
            for i in range(self._led.numLEDs):
               self._led.set(i, self._colors[int(((self._step + i)/3) % len(self._colors))])
            #Increment the internal step by the given amount
	if cycle == 2:
	   col = int(math.floor(self._step /  (len(self._colors)-1)))% len(self._colors)
           #print col
	   self._led.fill( self._colors[col])

        self._step += amt

#create driver for a 12 pixels
driver = DriverLPD8806(150, c_order = ChannelOrder.BRG)
led = LEDStrip(driver)

anim = StripTest(led)
anim.run()
