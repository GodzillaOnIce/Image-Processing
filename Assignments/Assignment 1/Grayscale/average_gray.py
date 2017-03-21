# Averaging is the most common grayscale conversion routine
# Calculates the average of the sum of the RGB values

import sys
import read_img

def average(imagefile):
    [size, maximum, pixels] = read_img.image_reader(imagefile)
    output = open('average_grayscale.pgm', 'w')

    #create header for new image file
    header = "P2\n# CREATOR average_gray.py\n{0} {1}\n".format(size[0], size[1], maximum)
    output.write(header)

    # Averaging the RGB values
    for i in pixels:
        gray = (i[0] + i[1] + i[2])/3
        output.write("%d\n" % gray)

    output.close()

average(raw_input("Enter name of source image:"))
