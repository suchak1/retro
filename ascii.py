from PIL import Image
import math
import sys
import argparse
import os


def image2pix(image):
    raw = image.load()
    width, height = image.size[0], image.size[1]

    pix = [[list(raw[i, j]) for j in range(height)] for i in range(width)]
    return pix


def pix2image(pix):
    for j in range(height):
        for i in range(width):
            raw[i, j] = tuple(pix[i][j])


def rgb2lum(r, g, b):
    # luminosity standardized on scale [0, 1]
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", type=str, help="input filename")
parser.add_argument("-o", "--output", type=str, help="output filename")
parser.add_argument("-s", "--scale", type=int, help="ascii output size")
parser.add_argument("-a", "--ascii", type=int, help="ascii char use")


args = parser.parse_args()

if args.input == None or not os.path.isfile(args.input):
    print("Please specify valid input file. Ex: $ python3 ascii.py -i filename.png")
    quit()

ifile = args.input
ofile = args.output
scale = args.scale if args.scale else 45
ascii = " .'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@" if args.ascii and args.ascii > 0 else " ░▒▓█"


im = Image.open(ifile)
raw = im.load()
width, height = im.size[0], im.size[1]
awidth = width // scale
aheight = height // scale


numAscii = len(ascii)

j = 0

while j < height:
    line1 = ""
    i = 0
    while i < width-awidth:
        grayscale = []
        for k in range(i, i + awidth):
            r, g, b = raw[k, j]
            lum = rgb2lum(r, g, b)
            grayscale.append(round(lum * (len(ascii) - 1)))
        char = max(set(grayscale), key=grayscale.count)
        line1 += ascii[char]*(1 + round(width / height))

        i += awidth

    print(line1)
    j += aheight


# j = 0

# while j < height:
#     line2 = ""
#     i = 0
#     while i < width-awidth:
#         grayscale = [round(sum(raw[k, j][0:3]) / (255*3) *
#                            (len(ascii) - 1)) for k in range(i, i+awidth)]
#         char = round(sum(raw[i, j][0:3]) / (255*3) * (len(ascii)-1))
#         line2 += ascii[char]*(1+round(width/height))

#         i += awidth

#     print(line2)
#     j += aheight


# im.save("test.jpg")

# fix:
# multiprocessing
# autocontrast
# read in terminal size and use
# video to images
# gui
# website
