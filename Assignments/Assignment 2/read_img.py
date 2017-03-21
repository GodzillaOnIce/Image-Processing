#reads an image in a text format into components of:
#1. size of image
#2. maximum colour value
#3. the actual pixels as an array of integers

import sys

class Image(object):

    def __init__(self, source):
        self.source = source
        [size, mx, pixels] = image_reader(source)
        self.size = size
        self.mx = mx
        self.pixels = pixels
        self.length = len(pixels)
        red = []
        green = []
        blue = []
        self.red = red
        self.green = green
        self.blue = blue
        for i in pixels:
            red = i[0]
            green = i[1]
            blue = i[2]


def image_reader(imagefile):
    file = open(imagefile)
    data = file.readlines() #data is an array of lines in file

    # Retrieving specific data
    image_size = data[2]    #the third line tells use the image size (index 2)
    image_size = image_size.split(' ')  #split on space, converting into an array of length and height
    image_max = data[3] #the fourth line tells us the maximimum value of a particular colour (index 3)
    image_pixels = data[4:len(data)]    #the remaining lines are the pixel rgb values

    # Converting retrieved data to usable integers
    size = map(int, image_size) #converts each element in the image_size array to integers
    maximum = int(image_max)    #converts the single maximum value in image_max to an integers
    img = map(int, image_pixels)    #converts each pixel to an integer value

    # Formatting the array of pixels for processing

    pixels = [img[3 * i : 3 * ( i + 1)] for i in range(len(img)/3)]  #iterate as many times as the number of values/3
    #creates a list of lists with 3 values (RGB values)

    file.close()

    return [size, maximum, pixels]
