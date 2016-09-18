#!/usr/bin/env python
from PIL import Image
import sys

def b2a(b):
    s = ''
    while len(b) != 0:
        binbyte = b[:8]  # Get a byte
        s += chr(int(binbyte, 2)) # Convert it
        b = b[9:]  # Skip every 9th bit
    return s

# Load image data
img = Image.open(sys.argv[1])
w,h = img.size
pixels = img.load()

binary = ''
for y in xrange(h):
    for x in xrange(w):
        # Pull out the LSBs of this pixel in RGB order
        binary += ''.join([str(n & 1) for n in pixels[x, y]])
print b2a(binary)

