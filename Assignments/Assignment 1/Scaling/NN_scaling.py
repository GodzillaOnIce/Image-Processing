# Simplest and fastest implementation of image scaling technique

import sys
import read_img

def NN(imagefile, ratio):
    [size, maximum, pixels] = read_img.image_reader(imagefile)
    output = open('NN_scaling.pgm', 'w')

    width = int(size[0] * ratio)
    height = int(size[1] * ratio)
    out = [0] * width * height

    #create header for new image file
    header = "P2\n# CREATOR NN_scaling.py\n{0} {1}\n{2}\n".format(width, height, maximum)
    output.write(header)

    for j in range(height):
        for k in range(width):
            x = int(k/ratio)
            y = int(j/ratio)
            out[(j*width) + k] = pixels[(y * width/2) + x]

    for p in out:
        output.write("{0}\n{1}\n{2}\n".format(p[0], p[1], p[2]))

    output.close()

#imagefile_i = raw_input("Enter name of input file:")
ratio_i = int(raw_input("Enter ratio of scaling:"))
NN("pepe.ppm", ratio_i)
