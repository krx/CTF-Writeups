# CSAW Finals 2015: Mandiant - Forensics 300

For this challenge we are given a pdf file called `Mandiant.pdf`. The pdf is 76 pages long, and considering this is a 300 point challenge, the flag or any hint probably isn't sitting there in plain text, so I didn't bother going through it and went straight to `pdf-parser`

## PDF Analysis

The first thing I always do with `pdf-parser` is get a summary about what the pdf contains, so I run:

```bash
$ pdf-parser --stats Mandiant.pdf 
Comment: 3
XREF: 1
Trailer: 1
StartXref: 1
Indirect object: 734
  355: 2, 1, 5, 16, 14, 48, 50, 9, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 64, 66, 68, 72, 71, 75, 79, 82, 87, 86, 94, 95, 96, 97, 98, 100, 104, 113, 112, 117, 118, 119, 122, 123, 124, 125, 128, 129, 107, 116, 137, 135, 143, 144, 145, 146, 152, 151, 155, 158, 157, 165, 166, 167, 168, 169, 172, 177, 182, 187, 192, 191, 197, 198, 199, 202, 205, 208, 216, 215, 212, 219, 225, 224, 222, 229, 230, 244, 243, 250, 237, 253, 254, 255, 236, 256, 257, 258, 259, 260, 261, 262, 235, 264, 265, 266, 234, 248, 249, 273, 268, 282, 280, 277, 286, 287, 292, 290, 297, 296, 303, 304, 305, 306, 310, 308, 316, 323, 326, 320, 334, 336, 330, 340, 346, 343, 350, 353, 357, 360, 366, 365, 370, 363, 369, 374, 378, 377, 383, 389, 387, 392, 393, 386, 395, 401, 398, 411, 414, 405, 421, 418, 425, 429, 432, 435, 439, 443, 442, 449, 451, 453, 457, 462, 460, 469, 472, 476, 479, 484, 482, 487, 489, 492, 495, 498, 501, 505, 508, 511, 514, 517, 522, 524, 526, 528, 532, 534, 536, 539, 56, 54, 544, 548, 550, 551, 263, 552, 555, 557, 556, 561, 562, 559, 58, 563, 566, 569, 59, 571, 574, 575, 577, 70, 579, 578, 583, 584, 581, 586, 585, 590, 591, 588, 133, 592, 593, 595, 597, 599, 600, 233, 603, 604, 606, 608, 607, 612, 613, 610, 319, 614, 615, 617, 619, 620, 622, 624, 625, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 627, 689, 626, 690, 691, 692, 693, 700, 713, 718, 719, 722, 701, 704, 705, 706, 707, 708, 709, 710, 55, 711, 724, 715, 726, 730, 727, 703, 732, 733, 702, 734
 /Annot 48: 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 74, 89, 90, 91, 92, 93, 115, 139, 140, 141, 142, 154, 160, 161, 162, 163, 164, 194, 195, 196, 218, 227, 228, 246, 247, 284, 285, 299, 300, 301, 302, 368, 486
 /Catalog 1: 699
 /Embeddedfile 1: 3
 /Encoding 4: 553, 572, 716, 725
 /ExtGState 11: 149, 546, 543, 51, 52, 8, 565, 148, 53, 7, 729
 /F 1: 4
 /Font 59: 121, 127, 10, 12, 13, 558, 60, 61, 63, 77, 580, 78, 587, 111, 108, 109, 110, 213, 214, 223, 240, 241, 242, 238, 239, 269, 270, 271, 272, 278, 279, 291, 309, 315, 314, 609, 321, 322, 332, 333, 344, 345, 364, 388, 399, 400, 406, 407, 408, 409, 410, 419, 420, 448, 468, 521, 531, 62, 11
 /FontDescriptor 30: 49, 67, 120, 126, 130, 251, 327, 337, 371, 415, 452, 525, 554, 560, 573, 576, 582, 589, 594, 596, 598, 601, 602, 605, 611, 616, 618, 621, 714, 723
 /Group 85: 17, 65, 73, 80, 84, 88, 101, 105, 114, 138, 153, 159, 173, 178, 184, 188, 193, 203, 206, 210, 217, 226, 245, 274, 283, 293, 298, 311, 317, 325, 335, 341, 347, 351, 355, 358, 361, 367, 375, 380, 384, 390, 396, 402, 413, 422, 426, 430, 433, 437, 440, 444, 450, 458, 464, 470, 473, 477, 480, 485, 490, 493, 496, 499, 503, 506, 509, 512, 515, 519, 523, 529, 533, 537, 540, 541, 545, 549, 542, 567, 570, 564, 720, 728, 712
 /Mask 3: 547, 568, 717
 /Metadata 24: 131, 174, 179, 220, 231, 252, 275, 288, 294, 312, 328, 338, 348, 372, 381, 391, 403, 416, 423, 445, 454, 465, 698, 731
 /Outlines 1: 623
 /Page 76: 6, 57, 69, 76, 81, 85, 99, 102, 106, 132, 147, 156, 170, 175, 180, 185, 190, 200, 204, 207, 211, 221, 232, 267, 276, 289, 295, 307, 313, 318, 329, 339, 342, 349, 352, 356, 359, 362, 373, 376, 382, 385, 394, 397, 404, 417, 424, 427, 431, 434, 438, 441, 446, 455, 459, 466, 471, 474, 478, 481, 488, 491, 494, 497, 500, 504, 507, 510, 513, 516, 520, 527, 530, 535, 538, 697
 /Pages 18: 694, 695, 15, 83, 136, 183, 209, 696, 281, 324, 354, 379, 412, 436, 463, 483, 502, 518
 /XObject 17: 103, 134, 150, 171, 176, 181, 189, 186, 201, 331, 428, 447, 456, 461, 467, 475, 721
```

Ok, lots of data in this pdf, but the only thing I care about is that there's exactly 1 `Embeddedfile` inside, with an object id of `3`. The next step is to extract this out:

```bash
$ pdf-parser --object 3 --raw --filter Mandiant.pdf > out
$ cat out
obj 3 0
 Type: /Embeddedfile
 Referencing: 2 0 R, 1 0 R
 Contains stream

  <<
    /Filter /FlateDecode
    /Length 2 0 R
    /Params 1 0 R
    /Type /Embeddedfile
  >>

 iVBORw0KGgoAAAANSUhEUgAAAmIAAAHTCAYAAACEKHSrAAAgAElEQVR4XuxdB3hTVRt+k7RJV7on
HRQou2UVyt57yhJEHAgOwL3Brb+/83fjBLeIqOyNbBApe28KpUD33m2S/s97wi2hNslNSbFgvsfY
0tx77jnfOfd87/mmArc+WwEHOTjg4ICDAw4OODjg4ICDAw4OXHcOKBxA7Lrz3PFABwccHHBwwMEB
BwccHHBwQHDgChDbsxrITa+WLQoooFAqxHcVFRXiw78plUpU4LJCzeQHv4f0dzOM5v38z3itdeKz
DAaD9QsdV1jkQEhwCHz9fCuvGT9+PPz9/f92T8KZBGTnZDu4aQMHQkNDERwcbMMdjksdHHBw4N/O
gYyMDMyfP7+SDa1iWqF7j+7/drbc9ONPyMzH/zYergLENvwEZF782+AVCgX4UavV4rvy8nIBiAiM
+DcBuQyGSoDGa/R6vVXQpFKpRLs6nc4qw3mds7OzuNYBxqyyy+IFkZGRCAoKqrzm0UcfRb169f52
...
...
...
x4sI8dMySBy2XENnmQEdPIRxPI8/RoagOQt+AR04lUizChQRiOzK7YdS7zQLt+89b25l2FeUlrG2
/Z8yZMjn6WgduGKzTl/gPR2x/W2iR4/t4+lmb147sChZ/sXRZq8OM4k+8RDPG3QlKa/UqOVoRb5W
TdkVgP3DsnHQ9oPv3sb9K6KT36aCfR7ozn2kZYDkgaomC/OAnD8nBec0OnfijTJ58BkxGwM0QtO+
Yr9unQ30UKsxIwpS0tPq4Rylt4RaKM43Zg9BKB46IRfgakbWbUBiz8QK6thmtCkffNuI1BdqM9lI
2IKyJpLjkcjY8RevZaBOz8lkkGpncCCODvOSw5zWOf2LGQABBAYAAQnAx6oABwsBAAEhIQEIDMAH
5AAICgGHU/ArAAAFARkIAAAAAAAAAAARFwBzAGUAYwByAGUAdAAuAHQAeAB0AAAAGQQAAAAAFAoB
AABLSvHvFdEBFQYBACAAAAAAAA==
```

Ok we're onto something, the extracted data contains some pdf-parser related text, and a few thousand line long base64 string. Let's decode this data and see what it is:

**NOTE:** I deleted the extra text from the beginning of `out`, leaving only the base64 data

```bash
$ base64 -d < out > out2
$ file out2
out2: PNG image data, 610 x 467, 8-bit/color RGBA, non-interlaced
$ mv out2 pic1.png
```

The data decoded to a PNG file, let's see what it is:

![alt text](https://raw.githubusercontent.com/kareemroks101/CTF-Writeups/master/CSAW%2015%20Finals/for300%20-%20Mandiant/pic1.png "pic1.png")

Hah, what a meme!

Anyway, let's keep looking in the picture's data

## PNG Analysis

Looking through the hex dump for the image, I found something interesting

```bash
$ tail pic1.png | xxd
...
...
...
0000360: f392 c39c d639 fd8b 1900 0104 0600 0109  .....9..........
0000370: c0c7 aa00 070b 0100 0121 2101 080c c007  .........!!.....
0000380: e400 080a 0187 53f0 2b00 0005 0119 0800  ......S.+.......
0000390: 0000 0000 0000 0011 1700 7300 6500 6300  ..........s.e.c.
00003a0: 7200 6500 7400 2e00 7400 7800 7400 0000  r.e.t...t.x.t...
00003b0: 1904 0000 0000 140a 0100 004b 4af1 ef15  ...........KJ...
00003c0: d101 1506 0100 2000 0000 0000            ...... .....
```

secret.txt? Looks like there's something else contained in this file

```bash
root@kali-kareem:~/Desktop/csaw15/Mandiant# binwalk pic1.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 610 x 467, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed, uncompressed size >= 229376
160173        0x271AD         7-zip archive data, version 0.4
```

Great, there's a 7zip archive inside. I pulled it out manually with a hex editor, now let's see what's inside

```bash
$ 7z x secret.7z 

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,4 CPUs)

Processing archive: secret.7z

Extracting  secret.txt

Everything is Ok

Size:       58375
Compressed: 43849
$ cat secret.txt 

/9j/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8Q
EBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQ
EBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wgARCAEbAUEDASIAAhEBAxEB/8QAHQAAAAcBAQEA
AAAAAAAAAAAAAAIDBAUGBwEICf/EABkBAAMBAQEAAAAAAAAAAAAAAAABAgMEBf/aAAwDAQACEAMQ
AAABprPTI7y/WpRPStY6uPFUPaFPqPMKvr+FDygl7Hx5nm6O9/eMnvCsfdFfvn8Wm+gVZceI1/oN
FB4UN7uIq8Oym9WsryG+9y5g58yj1jms6ZbTfoBUk/GiP0PyJryvFe0cQnXMDfQag1n4376M2sXg
...
...
...
ZE9Jek9FbmduRVZuRHNGOGN4N1JoMGNoOGVlTlMxK2syMks5Vzd6SnZ3eERJcityd2c5SXhMRzV4
cWc4R3ZVTldwUkNlR3ZNTjRXWTlkZWlrMnlhZmZZYXJFT3djMVBFd2dHcXFrYi9YNk9CVzlWa0xq
V1hvR3p4VWNwUlFpYldTdytORGVRWWl1SHJrTU1QU0dIeldJNGZNa3poeHNKUXJaRVB4RUJPRTdL
bUFEd2h4azdpYkNoVC9uMkJOZ041V3Q1WGFISUlNNk5EVE1ZbkRZeWU2U2JuVjZiSkZEY3hKVUp2
a1lFWDE1dEZWdUplZGNtY1hXZ0tWa0FFMndqbjRwbHJpcGI4ZUxJZ3hkOEVNOXpRVWptWE1BQUhH
UFBxdURELzN3bVIweTBwUTErNzdXemNOSlQ1OVlPWVVTYkJEYm5rc3FxTDRTVnQ2Q3IwVW9Yd25Q
UG9MWEtoVFZrdEVDbVVCNzMzcmRKMlpzWTZqM1hyNWptaFNsZk1TNTZOU3MyeWhPR29KSmxhQUx3
K0U0OQ0K
```

Ok, secret.txt contains <1000 lines of what looks to be more base64 data. Let's decode it and see what it is

```bash
$ base64 -d < secret.txt > out3
$ file out3
out3: JPEG image data, progressive, precision 8, 321x283, frames 3
$ mv out3 pic2.jpg
```

Another picture, this time a JPG, let's see what it is

![alt text](https://raw.githubusercontent.com/kareemroks101/CTF-Writeups/master/CSAW%2015%20Finals/for300%20-%20Mandiant/pic1.png "pic2.jpg")

Hahaha, these sure are great!

Still no flag, let's keep looking

## JPG Analysis

Looking at the hex dump / strings again, I found more base64 data appended to the end of the image:

```bash
root@kali-kareem:~/Desktop/csaw15/Mandiant# strings pic2.jpg 
	xG9
b#o]
Y2EB
 V~D
...
...
5TZ"
^p91b
D^sJ
"aKxw
S#UH
VVGEC8uGDQuNhhk6FKg0ICF9jVAUS54zurveSzXcwE9MsIHIZPuvP6vrSDgwULy5Kvm/wPe3zxddM4SSPgvWIg==
XQN6Y6QIpfofWw857i5DK71VV+AMw3qkl5fJBqvEToJVrzPmKDEgrBZOqPqIVFRqIhseBorGzt4AV+9AIjqf0SyN44jfglSbMEXyZMmxpQdIs72mTwoDhSCTHOuFsqBPRwmaj4Za/M5OFf9UIwBPKQBZYa++ZLok0ApDrHRKQxJIhOqYmHwBMAwT8LK6Ej/wy1gJzG/4k4kRCAlcu3Ks39FCJeamjV5t1Agx1zLBKTsaVBfD4FMVgLGzuu9AknZFceqd9j1KybcFRb2suI1CxUlSpsIJggSnZzgLTA8kDJVPKy8
...
...
+rwg9IxLG5xqg8GvUNWpRCeGvMN4WY9deik2yaffYarEOwc1PEwgGqqkb/X6OBW9VkLjWXoGzxUcpRQibWSw+NDeQYiuHrkMMPSGHzWI4fMkzhxsJQrZEPxEBOE7KmADwhxk7ibChT/n2BNgN5Wt5XaHIIM6NDTMYnDYye6SbnV6bJFDcxJUJvkYEX15tFVuJedcmcXWgKVkAE2wjn4plripb8eLIgxd8EM9zQUjmXMAAHGPPquDD/3wmR0y0pQ1+77WzcNJT59YOYUSbBDbnksqqL4SVt6Cr0UoXwnPPoLXKhTVktECmUB733rdJ2ZsY6j3Xr5jmhSlfMS56NSs2yhOGoJJlaALw+E49
```

This time there are two separate base64 strings here, let's decode them:

**NOTE:** I extracted the two base64 strings to `b1` and `b2`

```bash
$ base64 -d < b1 > o1
$ file o1
o1: data
$ xxd o1
0000000: 5551 840b cb86 0d0b 8d86 193a 14a8 3420  UQ.........:..4 
0000010: 217d 8d50 144b 9e33 babb de4b 35dc c04f  !}.P.K.3...K5..O
0000020: 4cb0 81c8 64fb af3f abeb 4838 3050 bcb9  L...d..?..H80P..
0000030: 2af9 bfc0 f7b7 cf17 5d33 8492 3e0b d622  *.......]3..>.."


$ base64 -d < b2 > o2
$ file o2
o2: data
$ xxd o2
0000000: 5d03 7a63 a408 a5fa 1f5b 0f39 ee2e 432b  ].zc.....[.9..C+
0000010: bd55 57e0 0cc3 7aa4 9797 c906 abc4 4e82  .UW...z.......N.
0000020: 55af 33e6 2831 20ac 164e a8fa 8854 546a  U.3.(1 ..N...TTj
0000030: 221b 1e06 8ac6 cede 0057 ef40 223a 9fd1  "........W.@":..
0000040: 2c8d e388 df82 549b 3045 f264 c9b1 a507  ,.....T.0E.d....
...
...
0003430: 4cb4 a50d 7eef b5b3 70d2 53e7 d60e 6144  L...~...p.S...aD
0003440: 9b04 36e7 92ca aa2f 8495 b7a0 abd1 4a17  ..6..../......J.
0003450: c273 cfa0 b5ca 8535 64b4 40a6 501e f7de  .s.....5d.@.P...
0003460: b749 d99b 18ea 3dd7 af98 e685 295f 312e  .I....=.....)_1.
0003470: 7a35 2b36 ca13 86a0 9265 6802 f0f8 4e3d  z5+6.....eh...N=
```

Now `file` yields nothing, and the data doesn't look like any particular file type. Where to go from here? Well, I had no idea, I was stuck, and apparently so was every other team that tried this problem. No progress was made until a new hint was released, which told us to check out something called `Free File Camouflage`

I looked up and downloaded this program, and opened the JPG with it

![alt text](https://raw.githubusercontent.com/kareemroks101/CTF-Writeups/master/CSAW%2015%20Finals/for300%20-%20Mandiant/ffc.png "Free File Camouflage")

This program extracted a file called `a.out`

## Last Step
Running `file` reveals that `a.out` is a 64-bit ELF, so let's run it:
```bash
root@kali-kareem:~/Desktop/csaw15/Mandiant# file a.out 
a.out: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=2e4595f77d1c1c460c3e43fd231f82621e035b90, not stripped
root@kali-kareem:~/Desktop/csaw15/Mandiant# ./a.out 
hello world, i found this flag under some bit-maps....
[HAVE A FLAG]
	flag{s3v3r4l_l4y3r5_d33p_&_2m4ny_l4yers_w1d3}
```

Finally! We now have our flag:
```
flag{s3v3r4l_l4y3r5_d33p_&_2m4ny_l4yers_w1d3}
```

# Closing Note
These great r2 memes are brought to you courtesy of itsZN

More memes can be found [here](https://www.reddit.com/r/r2memes/)