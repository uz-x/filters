# pyfilters

Adding filters to images in Python with the Pillow library.

## How to how filters picture how?

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

## Will there be a library soon?

Hopefully.  

## How did you make this?

These filters are all calculated by me. Each image starts from an entirely blank canvas and it fills in every single pixel one-by-one.

### bw

The black and white filter uses the same system as [my other website](https://testing.hrant.repl.co/bright-or-dark/) which uses RGB values to figure out if a color is light or dark. You can see the calculations at the website.

### invert

...
