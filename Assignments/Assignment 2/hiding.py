import sys
import math

def hide(message):
    file = open(message)
    data = file.readlines()
    maximum = 0
    buff = open('buffer.txt', 'w+')
    for i in xrange(len(data)):
        eq = data[i]
        for j in xrange(len(eq)):
            enc = ord(eq[j])
            buff.write('%d\n' % enc)
            if enc > maximum:
                maximum = enc
    buff.close()
    buff = open('buffer.txt')
    buff_data =  buff.read()
    xandy = int(round(math.sqrt(len(buff_data))))
    size = [xandy, xandy]

    out = open('encoded.pgm', 'w')
    header = "P2\n# CREATOR hiding.py\n{0} {1}\n{2}\n".format(size[0], size[1], maximum)
    out.write(header)
    out.write(buff_data)
    #for i in xrange(len(buff_data)):
        #eqb = buff_data[i]
        #for j in xrange(len(eqb)):
            #out.write('%d\n' % eqb[j])

    file.close()
    out.close()

hide('source.txt')
