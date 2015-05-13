# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:00:52 2014

@author: d1v8
"""
from PIL import Image

def neg_rgb(tuple_in):
    """(tuple)-> tuple
    
    Precondition: input must be a list or tuple of numbers    
    
    Returns the negative rgb values as a tuple

    >>> neg_rgb((0, 55, 100))
    (255, 200, 155)

    >>> neg_rgb([155, 10, 200])
    (100, 245, 55)
    
    """
    list_in = list(tuple_in)
    neg = []
    for i in list_in:
        i = 255 - i
        neg.append(i)
    neg = tuple(neg)    
    return neg

image = Image.open("baboon.png")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        get_rgb = image.getpixel((x,y))
        new_rgb = neg_rgb(get_rgb)
        image.putpixel((x,y), new_rgb)
    
image.save("baboon_neg.png")