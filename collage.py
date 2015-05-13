from PIL import Image

import negative
import grey

def channel_zero(pixels, channel_off):
    rgb = image.getpixel(pixels)
    rgb = list(rgb)
    rgb[channel_off] = 0
    rgb = tuple(rgb)
    return rgb  

image = Image.open("test_image.jpg")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        if x <= (width/2) and y <= (height/2):
            pix = image.getpixel((x,y))
            neg = negative.neg_rgb(pix)
            image.putpixel((x,y), neg)
        elif x <= (width/2) and y > (height/2):
            no_green = channel_zero((x,y), 1)
            image.putpixel((x,y), no_green)
        elif x > (width/2) and y > (height/2):
            pix = image.getpixel((x,y))
            avg = grey.average_rgb(pix)
            image.putpixel((x,y), (avg, avg,avg))
        elif x > (width/2) and y <(height/2):
            pix = image.getpixel((x,y))
            no_blue = channel_zero((x,y), 2)
            image.putpixel((x,y), no_blue)
            
            
image.save("collage.png")

