import random
import time
import os

try:
    from PIL import Image
except:
    os.system("pip install Pillow")

def random_string(length):
    chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890---")
    final = ""
    for i in range(length):
        final += chars[random.randint(0, len(chars)-1)]
    return final

def draw_pixel(image, x, y, color):
    image.putpixel((x, y), color)

def create_image(width, height):
    return Image.new("RGBA", (width, height), "white")

def save_image(image, filename):
    image.save(filename)

def rgb_to_hex(rgb):
    alpha = min(max(rgb[3], 0), 255)
    hex_color = "#{:02x}{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2], alpha)
    return hex_color

estimated_times = {
    "bw": (3.22677+3.398) / 2,
    "invert": (2.8898 + 4.164) / 2,
    "0s": (3.27+3.910) / 2,
    "death": (3.1562+3.916) / 2,
    "90": (2.813+4.263) / 2,
    "180": (2.8344+3.74744) / 2
}

filename = input("Filename: ")
image = Image.open(filename)
filter = input("Filter: ")

print(f"Estimated time: {estimated_times[filter]} s")

starttime = time.time()

original_image = []
height = image.height
width = image.width

y = -1

for h in range(height):
    x = 0
    y += 1
    original_image.append([])
    for w in range(width):
        pixel_color = image.getpixel((x, y))
        original_image[h].append(pixel_color)
        x += 1

canvas = create_image(width, height)

if filter == "bw":
    for h in range(height):  # Iterate over the height (y values)
        for w in range(width):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            if sum(pixel_color) < 765/2:
                draw_pixel(canvas, w, h, (0, 0, 0, 255))
            elif sum(pixel_color) > 765/2:
                draw_pixel(canvas, w, h, (255, 255, 255, 255))
elif filter == "invert":
    for h in range(height):  # Iterate over the height (y values)
        for w in range(width):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            r_inverted = 255 - pixel_color[0]
            g_inverted = 255 - pixel_color[1]
            b_inverted = 255 - pixel_color[2]
            draw_pixel(canvas, w, h, (r_inverted, g_inverted, b_inverted, 255))
elif filter == "0s":
    for h in range(height):  # Iterate over the height (y values)
        for w in range(width):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            average = round(sum(pixel_color) / 3)
            draw_pixel(canvas, w, h, (average, average, average, 255))
elif filter == "death":
    for h in range(height):  # Iterate over the height (y values)
        for w in range(width):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            if pixel_color[0] < 20 and pixel_color[1] < 20 and pixel_color[2] < 20:
                draw_pixel(canvas, w, h, (pixel_color[0], pixel_color[1], pixel_color[2], 255))
            else:
                draw_pixel(canvas, w, h, (pixel_color[0]+100, abs(pixel_color[1]-70), abs(pixel_color[2]-70), 255))
elif filter == "pixel":
    am = int(input("Pixelation level: "))
    truey = -am

    for h in range(int(height/am)):  # Iterate over the height (y values)
        truey += am
        truex = -am
        for w in range(int(width/am)):
            truex += am  # Increment by 'am' instead of 2
            pixel_color = original_image[truey][truex]  # Get the pixel color at the current position

            for i in range(am):
                for j in range(am):
                    draw_pixel(canvas, truex+j, truey-i, (pixel_color[0], pixel_color[1], pixel_color[2], 255))
elif filter == "180":
    for h in range(height):  # Iterate over the height (y values)
        for w in range(width):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            draw_pixel(canvas, width - 1 - w, height - 1 - h, (pixel_color[0], pixel_color[1], pixel_color[2], 255))
elif filter == "90":
    canvas = create_image(height, width)
    for w in range(width):  # Iterate over the width (x values)
        for h in range(height):
            pixel_color = original_image[h][w]  # Get the pixel color at the current position
            draw_pixel(canvas, height - 1 - h, w, (pixel_color[0], pixel_color[1], pixel_color[2], 255))

names = {
    "bw": 'obaw',
    "invert": 'inverted',
    "0s": 'nosaturation',
    "death": 'death',
    "pixel": 'pixel',
    "180": '180deg',
    "90": '90deg'
}

name = names[filter]

save_image(canvas, f"{filename.replace('.png', '')}_{name}.png")

print(f"Real time: {time.time()-starttime} s")

print(f"Saved as {filename.replace('.png', '')}_{name}.png")

_ = input("")
