#!/usr/bin/env python3
import argparse
import unicornhat as UH
import time, math, colorsys
from random import randint
from collections import deque

parser = argparse.ArgumentParser(description='Pretty Patterns.')
parser.add_argument('-b','--brightness', type=float, dest='brightness', default=0.1, help='brightness')
parser.add_argument('-m','--max', type=int, dest='max', default=10, help='Max repeats of each pattern')

args = parser.parse_args()

UH.brightness(args.brightness)

while True:  
  
  #Circle - works not sure it looks good
  bank = deque([[255, 0, 0],[0, 255, 0],[0, 0, 255],[255, 255, 0],[0, 255, 255],[255, 0, 255]])
  for i in range(randint(0, args.max)):
    for y in range(8):
      for x in range(8):
        dist = math.floor(math.sqrt(((3.5 - x)*(3.5 - x))+((3.5 - y)*(3.5 - y)))/2)
        #print(y, x, dist)
        UH.set_pixel(x, y, bank[dist][0], bank[dist][1], bank[dist][2])
    UH.show()
    last = bank.pop()
    bank.appendleft(last)
    time.sleep(1)
  
  
  #RANDOM_SPARKLES 4x4
  for j in range(20 * randint(0, args.max)):
    x = randint(0, 1)
    y = randint(0, 1)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    for iy in range(4):
      for ix in range(4):
        UH.set_pixel((x*4)+ix  , (y*4)+iy,   r, g, b)
    UH.show()
    time.sleep(0.1)
  
  #Simple
  for i in range(randint(0, args.max)):
    r = randint(128, 255)
    g = randint(128, 255)
    b = randint(128, 255)
    for y in range(8):
      for x in range(8):
        UH.set_pixel(x,y,r,g,b)
      UH.show()
      time.sleep(0.05)
    time.sleep(1)
    #UH.clear()
  
  
  #RANDOM_SPARKLES 2x2
  for j in range(500 * randint(0, args.max)):
    x = randint(0, 3)
    y = randint(0, 3)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    UH.set_pixel((x*2)  , (y*2),   r, g, b)
    UH.set_pixel((x*2)+1, (y*2),   r, g, b)
    UH.set_pixel((x*2)  , (y*2)+1, r, g, b)
    UH.set_pixel((x*2)+1, (y*2)+1, r, g, b)
    UH.show()
    

  #rainbow
  i = 0.0
  offset = 50
  for j in range(100 * randint(0, args.max)):
    i = i + 0.3
    for y in range(8):
      for x in range(8):
        r = 0#x * 32
        g = 0#y * 32
        xy = x + y / 4
        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
        r = max(0, min(255, r + offset))
        g = max(0, min(255, g + offset))
        b = max(0, min(255, b + offset))
        UH.set_pixel(x,y,int(r),int(g),int(b))
    UH.show()
    time.sleep(0.01)


