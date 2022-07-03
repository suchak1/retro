import cv2
from glitch_this import ImageGlitcher
from PIL import Image
import numpy as np

# mix vids frame by frame
# 10s full pic, 5s zoomed in
# block.mp4
ascii = cv2.VideoCapture(
    '/mnt/c/Users/sucha/Videos/Captures/ascii.mp4')
block = cv2.VideoCapture(
    '/mnt/c/Users/sucha/Videos/Captures/block.mp4')


def get_frames(vidcap):
    ret, frame = vidcap.read()
    frames = []
    while ret:
        frames.append(frame)
        ret, frame = vidcap.read()
    return frames


ascii_frames = get_frames(ascii)
print(len(ascii_frames))
# print(ascii_ret)
# print(ascii_frame)
# print(type(ascii_frame))
# print(len(ascii_frame))

block_frames = get_frames(block)
print(len(block_frames))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(
    '/mnt/c/Users/sucha/Videos/Captures/final1.mp4',
    fourcc, 26, (1920, 1080))


res_frames = []
for i in range(len(ascii_frames)):
    if i > 100 and i < 200:
        res_frames.append(ascii_frames[i])
        res_frames.append(block_frames[i])

res_frames += res_frames[::-1]


# new_frames = []
# for idx, frame in res_frames:
#     if

# res_frames = new_frames

ig = ImageGlitcher()


def glitch(frame):
    img = Image.fromarray(frame)
    ig.inputarr = np.asarray(img)
    ig.outputarr = np.array(img)
    ig.seed = None
    # ig.img_mode = 'RGB'
    ig.pixel_tuple_len = len(img.getbands())
    ig.img_width, ig.img_height = img.size
    ig.img_mode = img.mode
    img = ig._ImageGlitcher__get_glitched_img(1.1, 1, False)
    frame = np.asarray(img)
    return frame


for frame in res_frames:
    frame = glitch(frame)
    # frame = cv2.resize(frame, (854, 480), fx=0, fy=0,
    #                    interpolation=cv2.INTER_CUBIC)
    writer.write(frame)

ascii.release()
writer.release()
