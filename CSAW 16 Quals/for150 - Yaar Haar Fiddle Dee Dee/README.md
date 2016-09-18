# CSAW Quals 2016: Yaar Haar Fiddle Dee Dee - Forensics 150

>DO WHAT YE WANT 'CAUSE A PIRATE IS FREE. YOU ARE A PIRATE!

For this challenge we are given the network capture [for200.pcapng](https://drive.google.com/open?id=0B8D2vqg5KC_oX2ZROWZRZ3hIdlk).

## PCAP Analysis

There was only one stream of interest from this capture that contained a few MB of base64, and a couple clues. So I just save that stream and we're done with the pcap.

The important thing to note here is that there are **3** separate base64'd files here:

* A ~6MB jpg, which turns out to be 1003 jpgs `cat`'d together
* A password protected zip that contains `flag.txt`
* An OpenCV Haar Cascade

The clues and files in the stream can be summarized like this:

```
yaaaaaaaar, land ho!
    Hey wesley, you got that flag?
Ayy, I got yer files right here, matey!

            [base64'd jpg]
            [base64'd flag.zip]

And here be the map to the booty!

            [base64'd Haar cascade]

    I don't understand, this isn't even a ma-
Yarrrr, the booty be buried by that which the map points to! (no spaces and no caps)
Ayy, now I be off. But remember, the factor of scales be 1.02, and the neighborly sorts be limited to 50!
Lastly, if ye sail the seven seas, you do be a pirate!
```

## Separate the files

First thing to do is separate the three chunks of base64 (I saved them as `b{1..3}` here) and decode them:

```bash
$ base64 -d b1 > out.jpg
$ base64 -d b2 > flag.zip
$ base64 -d b3 > cascade.xml
```

Then seperate all of the jpgs using `foremost` (or `binwalk`, `scalpel`, etc.):

```bash
$ foremost out.jpg
Processing: out.jpg
|*|
```

## Solution

The goal is to find the password to `flag.zip`, and the clues hint at how to do this. It refers to the OpenCV cascade as a "map", and hints that the password is "what the map points to (no spaces and no caps)". So we need to run the cascade against all of the pictures, and hopefully whatever it detects will be our password.

I wrote a quick script to run the cascade against all images and save what it detects. Another part of the clue came into play here:

```
But remember, the factor of scales be 1.02, and the neighborly sorts be limited to 50!
```

These values are parameters to `CascadeClassifier.detectMultiScale`, so I make use of those here:

```python
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
```

This didn't work perfectly on the first try, it detected around 9 images. I kept bumping up `min_neighbors` until eventually only one image was detected:

![X](./00004739.jpg)

So the password comes out to be `skullandcrossbones`, and we get the flag:

```
flag{b31Ng_4_P1r4tE_1s_4lR1GHT_w1Th_M3}
```
