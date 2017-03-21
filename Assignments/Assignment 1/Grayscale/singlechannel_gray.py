# Fastest computational method for grayscale reduction
# Simply grabs a single channel (red/green/blue) and call that the grayscale one

import sys
import read_img

def single_channel(imagefile):
    [size, maximum, pixels] = read_img.image_reader(imagefile)
    #sets the variables on the left to the returned values of the image_reader

    #create header for output file(s)
    header = "P2\n# CREATOR: singlechannel_gray.py\n{0} {1}\n{2}\n".format(size[0], size[1], maximum)

    #open files to be written to
    r = open('r_singlechannel.pgm', 'w')
    g = open('g_singlechannel.pgm', 'w')
    b = open('b_singlechannel.pgm', 'w')

    #write headers of each .pgm file
    r.write(header)
    g.write(header)
    b.write(header)

    #Extract single channel and write to file
    for i in pixels:
        r.write("%d\n" % (i[0])) #red is the first index
        g.write("%d\n" % (i[1])) #green is the second index
        b.write("%d\n" % (i[2])) #blue is the third index

    r.close()
    g.close()
    b.close()

single_channel(raw_input("Enter name of source image:"))
