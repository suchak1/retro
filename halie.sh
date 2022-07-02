#!/bin/bash

set -e

ASCII_OUTPUT=$(python3 ascii.py -i im.jpeg -s 57)
# echo "${ASCII_OUTPUT}"
convert label:"${ASCII_OUTPUT}" test.png


# convert to ascii letters and screen record portion of screen, then zoom in and end recording
# zoom in on "I love you. ❤️"
# reverse footage and add to end

# python3 ascii.py -i im_dramatic.jpeg -s 160

# * THIS ONE
#  python3 ascii.py -i im_dramatic.jpeg -s 110 
# photomosh.com
# jitter effect/filter

# vivid and dramatic(*)


# full screen,
# press ctrl + 20-30 times (do 25?)
# 2.5 sec on i love you, press esc, wait 5 sec