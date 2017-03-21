import sys
import read_img
import correct_gray

def Back_Sub(back, front):

    output = open('back_subtraction.pgm', 'w+')

    #create header for new image file
    header = "P2\n# CREATOR back_sub.py\n{0} {1}\n{2}\n".format(sizeb[0], sizeb[1], maximumb)
    output.write(header)

    # Applying the formula
    for i in xrange(len(front)):
        #for j in xrange(len(front[i])):
        diff = abs(front[i] - back[i])
        if diff > threshold:
            output.write("{0}\n".format(diff))
        else:
            output.write("0\n")

def correct_back(imagefile_back):
    [size, maximum, pixels] = read_img.image_reader(imagefile_back)
    output = open('correct_back.pgm', 'w+')

    #create header for new image file
    header = "P2\n# CREATOR correct_back.py\n{0} {1}\n{2}\n".format(size[0], size[1], maximum)
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

def correct_front(imagefile_front):
    [size, maximum, pixels] = read_img.image_reader(imagefile_front)
    output = open('correct_front.pgm', 'w+')

    #create header for new image file
    header = "P2\n# CREATOR correct_front.py\n{0} {1}\n{2}\n".format(size[0], size[1], maximum)
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

def imagereader_gray(imagefilei):
    file = open(imagefilei)
    data = file.readlines() #data is an array of lines in file

    # Retrieving specific data
    image_size = data[2]    #the third line tells use the image size (index 2)
    image_size = image_size.split(' ')  #split on space, converting into an array of length and height
    image_max = data[3] #the fourth line tells us the maximimum value of a particular colour (index 3)
    image_pixels = data[4:len(data)]    #the remaining lines are the pixel rgb values

    # Converting retrieved data to usable integers
    size = map(int, image_size) #converts each element in the image_size array to integers
    maximum = int(image_max)    #converts the single maximum value in image_max to an integers
    pixels = map(int, image_pixels)    #converts each pixel to an integer value

    # Formatting the array of pixels for processing

    #pixels = [img[3 * i : 3 * ( i + 1)] for i in range(len(img)/3)]  #iterate as many times as the number of values/3
    #creates a list of lists with 3 values (RGB values)

    #file.close()

    return [size, maximum, pixels]

#back_input = correct_gray.correct('back.ppm')
#front_input = correct_gray.correct('front.ppm')
back_gray = correct_back('back.ppm')
front_gray = correct_front('front.ppm')

[sizeb, maximumb, back_input] = imagereader_gray('correct_back.pgm')
[sizef, maximumf, front_input] = imagereader_gray('correct_front.pgm')
threshold = 15
Back_Sub(back_input, front_input)
