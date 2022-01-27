from tkinter import *
from PIL import Image

wtrmrk = Image.open("watermark.png")
im = Image.open("mynft.png")

# Use this to select entire image 'uploaded' by user (add watermark on top later)
entire_image = (0, 0, im.size[0], im.size[1])

# Center of image
xsize, ysize = im.size

xcenter, ycenter = (xsize // 2 - 100), (ysize // 2)
top_left = (xsize // 4 - 100, ysize // 4)
top_right = (round(xsize * .75 - 100), ysize // 4)
bottom_left = (xsize // 4 - 100, round(ysize * .75))
bottom_right = (round(xsize * .75 - 100), round(ysize * .75))


canvas = Image.new("RGBA", im.size, (255, 255, 255, 0))
watermark_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))

canvas.paste(im=im)

watermark_layer.paste(im=wtrmrk, box=(xcenter, ycenter), mask=wtrmrk)
watermark_layer.paste(im=wtrmrk, box=top_left, mask=wtrmrk)
watermark_layer.paste(im=wtrmrk, box=top_right, mask=wtrmrk)
watermark_layer.paste(im=wtrmrk, box=bottom_left, mask=wtrmrk)
watermark_layer.paste(im=wtrmrk, box=bottom_right, mask=wtrmrk)

image_blend = Image.blend(canvas, watermark_layer, .15)
image_blend.show()

image_blend.save("watermarked_image.png")

