import argparse

parser = argparse.ArgumentParser(description='Party Lights Strips of LPD8806.')
#parser.add_argument('-b','--brightness', type=float, dest='brightness', default=0.1, help='brightness')
parser.add_argument('-l','--length', type=int, dest='length', default=160, help='Length of strip')
parser.add_argument('-r','--random', type=bool, dest='random', nargs='?', const=True, default=False, help='Random')

args = parser.parse_args()

from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
from bibliopixel.animation import *
from strip_animations import *
import random

driver = DriverLPD8806(args.length, c_order = ChannelOrder.BRG)
led = LEDStrip(driver)
iFPS = 20
iSecondsPerAnim = 10
animations = []


#Rainbow(led, start=0, end=-1)
#RainbowCycle(led, start=0, end=-1)
#ColorPattern(led, colors, width, dir = True, start=0, end=-1)
#ColorWipe(led, color, start=0, end=-1)
#ColorFade(led, colors, step = 5, start=0, end=-1)
#ColorChase(led, color, width=1, start=0, end=-1)
#PartyMode(led, colors, start=0, end=-1)
#FireFlies(led, colors, width = 1, count = 1, start=0, end=-1)
#LarsonScanner(led, color, tail=2, start=0, end=-1)
#LarsonRainbow(led, tail=2, start=0, end=-1)
#Wave(led, color, cycles, start=0, end=-1)
#WaveMove(led, color, cycles, start=0, end=-1)
#RGBClock(led, hStart, hEnd, mStart, mEnd, sStart, sEnd)


coloursRainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]
coloursUTC = [colors.Turquoise, colors.Green, colors.Blue, colors.Indigo]


try:
    animations.append([Rainbow(led), 20])
    animations.append([LarsonRainbow(led), 20])
    animations.append([PartyMode(led, coloursRainbow , 3),4])
    animations.append([ColorPattern(led, coloursUTC, 30), 10])
    animations.append([RainbowCycle(led), 20])
    
    animations.append([FireFlies(led, coloursRainbow , 20),20])
    animations.append([LarsonRainbow(led, 10),  20])
    animations.append([PartyMode(led, coloursUTC),4])
    animations.append([ColorWipe(led, colors.Blue),20])
    animations.append([ColorFade(led, coloursUTC, 10), 20])
    animations.append([FireFlies(led, coloursUTC , 20),50])
    animations.append([ColorPattern(led, coloursUTC, 30), 10])
    
    
    while len(animations) > 0:
        led.all_off()
        if args.random :
            anim = random.choice(animations)
        else :
            anim = animations.pop()
        
        #anim).run(fps = iFPS, max_steps = (iFPS * iSecondsPerAnim) )
        #anim.run(fps = iFPS, max_steps = ( led.numLEDs * 2 ))
        anim[0].run( untilComplete = True, fps = anim[1], max_cycles = 1 )
    
    print "done!"

except KeyboardInterrupt:
    pass

led.all_off()
led.update()