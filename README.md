# filters

Adding effects to images in Python with the Pillow library.

## How to how effects picture how?

Place your target image in the same directory as the Python file, and run it.

## What filters are there?

These are all the current filters:  
  
**bw:** Only black and white. No grays.  
**invert:** Inverts all colors.  
**0s:** No saturation (bw but with grays).  
**death:** vewy scewy aaa (turns it a bit more red)  
**pixel:** Pixelates the image.  
**90:** Rotates the image 90 degrees.  
**180:** Rotates the image 180 degrees.  

## Syntax

```
Filename: your_image.png
Filter: (bw, invert, 0s, ...) (pick one)
```

If you pick pixel:

```
Pixelation level: (If you write 20, the pixels will look like 20x20 squares. It does not resize the actual image.)
```
