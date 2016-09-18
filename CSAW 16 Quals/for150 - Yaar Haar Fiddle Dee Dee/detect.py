#!/usr/bin/env python

import os
import sys
import cv2

# Get all of the pictures
imgs = os.listdir('images')

# Cascade we'll be using for detection
cascade = cv2.CascadeClassifier('cascade.xml')

# From the clues
scaling_factor = 1.02
min_neighbors = 70  # Bumped this up until one pic was left

for img_name in imgs:
    # Load the image and run the cascade
    img = cv2.imread(os.path.join('images', img_name))
    detect = cascade.detectMultiScale(img, scaling_factor, min_neighbors)
    if len(detect) > 0:
        for (x, y, w, h) in detect:
            # X marks the spot!
            cv2.line(img, (x, y),     (x + w, y + h), (255, 0, 0), 2)
            cv2.line(img, (x, y + h), (x + w, y),     (255, 0, 0), 2)
        # Save the new image
        cv2.imwrite(os.path.join('detected', img_name), img)

