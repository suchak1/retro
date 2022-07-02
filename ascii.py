from PIL import Image, ImageDraw, ImageFont
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
lines = []
while j < height:
    line = ""
    i = 0
    while i < width-awidth:
        grayscale = []
        # reds = []
        # greens = []
        # blues = []
        for k in range(i, i + awidth):
            r, g, b = raw[k, j]
            lum = rgb2lum(r, g, b)
            grayscale.append(round(lum * (len(ascii) - 1)))
        char = max(set(grayscale), key=grayscale.count)
        line += ascii[char] * (1 + round(width / height))

        i += awidth

    print(line)
    lines.append(line)
    j += aheight

im = Image.new(mode='RGB', size=(width, height))
draw = ImageDraw.Draw(im)
font_location = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
# font_location = '/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf'
# font-size: 1, scale: 800, 900
# font size: 5, scale: 300
# font size: 10, scale: 160 - this is good
# font-size: 15, scale: 110 - this is good *
#  python3 ascii.py -i im_dramatic.jpeg -s 110
# font-size: 20, scale: 85
# font-size: 30, scale: 60
font_size = {800: 1, 900: 1, 300: 5, 160: 10, 110: 15, 85: 20, 60: 30}[scale]
font = ImageFont.truetype(font_location, font_size)

mid_msg = "I love you. ❤️"
mid_idx = round(len(lines) / 2)
line = lines[mid_idx]

line = line[0: int(len(line) / 2 - len(mid_msg) / 2)] + \
    mid_msg + line[int(len(line) / 2 + len(mid_msg) / 2):]
lines[mid_idx] = line


for idx, line in enumerate(lines):
    draw.text((0, idx / len(lines) * height),
              line, fill=(255, 255, 255), font=font)
# draw.text((0, 100), "Hello, TutorialsPoint!", fill=(255, 0, 0), font=font)
# im.show()
filename = ifile.split('.')[0]
im.save(f"mod_{filename}{'_a' if args.ascii else ''}.jpg")

# fix:
# multiprocessing
# autocontrast
# read in terminal size and use
# video to images
# gui
# website
