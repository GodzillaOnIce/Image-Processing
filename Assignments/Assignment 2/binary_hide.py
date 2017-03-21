import sys
import binascii
import read_img


pepe = read_img.Image('pepe.ppm')
#print "{0}".format(pepe.name)
print "{0}".format(pepe.source)
out = open('sample.txt', 'w')
pix = pepe.pixels

for i in xrange(len(pix)):
    out.write(pepe.pix[i])

out.close()
