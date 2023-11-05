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

These filters are all calculated by me + a little bit of ChatGPT assistance. Each image starts from an entirely blank canvas and it fills in every single pixel one-by-one.

### bw

The black and white filter uses the same system as [my other website](https://testing.hrant.repl.co/bright-or-dark/) which uses RGB values to figure out if a color is light or dark. You can see the calculations at the website.

### invert

Let's say it scans a pixel and the color is `#5d26cd` which has the RGB values of `rgb(93, 38, 205)`.  
It gets the reverse values of each color by removing their value from 255:

```
255 - 93 (Old R value) = 162 (New R value)
255 - 38 (Old G value) = 217 (New G value)
255 - 205 (Old B value) = 50 (New B value)
```

### 0s

It calculates the average RGB value by adding them together and dividing the entire value by 3, then applies that color to the pixel.

### death

Increases the R value, decreases the G and B values.

### pixel

write this later

### 90

When we turn it 90 degrees, we want the pixel that was originally on 0 x and 0 y to be on 100 x and 0 y on a 100x100 canvas.  
It applies that logic to all pixels.

### 180

Same thing as 90 but 180. (very good explanatnion hahahaha yes)
