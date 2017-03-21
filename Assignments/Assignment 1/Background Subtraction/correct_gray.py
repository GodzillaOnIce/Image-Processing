# Grayscale using a formula to correct for the human eye
# gray = (red * 0.3 + green * 0.59 + blue * 0.11)

import sys
import read_img

def correct(imagefile):
    [size, maximum, pixels] = read_img.image_reader(imagefile)
    output = open('correct_grayscale.pgm', 'w+')

    #create header for new image file
    header = "P2\n# CREATOR correct_gray.py\n{0} {1}\n{2}\n".format(size[0], size[1], maximum)
    output.write(header)

    # Applying the formula
    for i in pixels:
        red = i[0]
        green = i[1]
        blue = i[2]
        # simply multiply by the ratios specified
        gray = (red * 0.3) + (green * 0.59) + (blue * 0.11)
        output.write("%d\n" % gray) #write to output file


    return output
    #output.close()  #close output file
