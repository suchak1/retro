import cv2

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
    '/mnt/c/Users/sucha/Videos/Captures/out.mp4',
    fourcc, 26, (1920, 1080))


for i in range(len(ascii_frames)):
    writer.write(ascii_frames[i])
    writer.write(block_frames[i])


ascii.release()
writer.release()
