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
			raw[i, j] = tuple(pix[i][j])#(pixNew[i][j][0], pixNew[i][j][1], pixNew[i][j][2])



parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", type=str, help="input filename")
parser.add_argument("-o", "--output", type=str, help="output filename")
parser.add_argument("-s", "--scale", type=int, help="ascii output size")
parser.add_argument("-a", "--ascii", type=bool, help="ascii char use")


args = parser.parse_args()

if args.input == None or not os.path.isfile(args.input):
	print("Please specify valid input file. Ex: $ python3 ascii.py -i filename.png")
	quit()

ifile = args.input
ofile = args.output
scale = args.scale if args.scale else 45

ascii=" ░▒▓█"

if args.ascii:
	ascii = " .'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"	

#ascii = ascii[::-1]


im = Image.open(ifile)
raw = im.load()
print(im.size)
width, height = im.size[0], im.size[1]
#scale = max(width, height) // 14
#scale = 45
awidth = width // scale
aheight = height // scale
#print(pix[0, 1079])
print(" ░▒▓█")


#ascii = ascii[::-1]

numAscii = len(ascii)
print(numAscii)
#print(pix)
#pix = image2pix(im)

j = 0

while j < height:
	line = ""
	i = 0
	while i < width-awidth:
		#print(i, j)
		#print(pix[i, j])
		#grayscale = [round(sum(pix[k][j][0:3]) / (255*3) * (len(ascii) - 1)) for k in range(i, i+awidth)]
		grayscale = [round(sum(raw[k,j][0:3]) / (255*3) * (len(ascii) - 1)) for k in range(i, i+awidth)]

		char = max(set(grayscale), key = grayscale.count)


		#char = round(sum(pix[i][j][0:3]) / (255*3) * (len(ascii)-1))
		line += ascii[char]*(1+round(width/height))
		i += awidth
	print(line)
	j += aheight

# while j < height:
# 	line = ""
# 	i = 0
# 	while i < width:
# 		#print(i, j)
# 		#print(pix[i, j])
# 		char = round(sum(raw[i, j][0:3]) / (255*3) * (len(ascii)-1))
# 		line += ascii[char]*(1+round(width/height))
# 		i += awidth
# 	print(line)
# 	j += aheight




# for i, x in enumerate(pix):
# 	for j, y in enumerate(x):
# 		if i < 500 and j < 500:
# 			y[0] += 100





#raw = pix2image(pix)
#im.save("krish3.jpg")

# for i in range(width):
# 	for j in range(height):
# 		if i < 500:
# 			pix[i,j] = (pix[i, j][0]+10+j, pix[i, j][1]+10+j, pix[i, j][2]+10+j)
#im.save("krish2.jpg")

#note: i is column, j is row

# fix:
# read in terminal size and use
# 2d array pix
# functions
# video to images
# gui
# website