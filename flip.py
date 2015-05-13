# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:00:52 2014

@author: d1v8
"""
from __future__ import print_function, division
import Image

image = Image.open("baboon.png")
width = image.size[0]
height = image.size[1]
flip = Image.new('RGB', (width, height))

for x in range(width):
    for y in range(height):
        rgb = image.getpixel((x,y))
        new_y = height - y - 1
        xy = (x, new_y)
        flip.putpixel(xy, rgb)
        
flip.save("baboon_flip.png")