# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:00:52 2014

@author: d1v8
"""
from __future__ import print_function, division
from PIL import Image

def average_rgb(tuple_in):
    """(tuple)-> int
    
    Precondition: input must be a list or tuple of numbers    
    
    Returns the average of the sum of the tuple or list.

    >>> average_rgb((0, 1, 2, 3, 4))
    2

    >>> average_rgb([0, 1, 2, 3, 4])
    2
    
    """
    list_in = list(tuple_in)
    sum = 0
    total = len(list_in)
    for i in list_in:
        sum += i
    average = int(sum/total)
    return average

image = Image.open("test_image.jpg")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        get_rgb = image.getpixel((x,y))
        new_grey = average_rgb(get_rgb)
        new_rgb = (new_grey, new_grey, new_grey)
        image.putpixel((x,y), new_rgb)
    
image.save("grey_image.png")