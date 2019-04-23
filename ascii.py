from PIL import Image
import math

#filename = "l3"
filename = "krish.jpg"
im = Image.open(filename)
pix = im.load()
print(im.size)
width, height = im.size[0], im.size[1]
#scale = max(width, height) // 14
scale = 45
awidth = width // scale
aheight = height // scale
#print(pix[0, 1079])
print(" ░▒▓█")


ascii = " .'`,^:\";~-_+<>i!lI?/\|()1{}[]rcvunxzjftLCJUYXZO0Qoahkbdpqwm*WMB8&%$#@"
#ascii = ascii[::-1]
ascii=" ░▒▓█"

numAscii = len(ascii)
print(numAscii)
#print(pix)

j = 0

while j < height:
	line = ""
	i = 0
	while i < width:
		#print(i, j)
		#print(pix[i, j])
		char = round(sum(pix[i, j][0:3]) / (255*3) * (len(ascii)-1))
		line += ascii[char]*(1+round(width/height))
		i += awidth
	print(line)
	j += aheight


for i in range(width):
	for j in range(height):
		if i < 500:
			pix[i,j] = (pix[i, j][0]+10+j, pix[i, j][1]+10+j, pix[i, j][2]+10+j)
#im.save("krish2.jpg")

#note: i is column, j is row

# fix:
# read in terminal size and use
# 2d array pix
# functions
# video to images
# gui
# website