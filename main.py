from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image


def open_file():
    file = askopenfile(mode='r', filetypes=[('Image Files', '*.png'), ('All Files', '*.*')])
    file.write("user_image.png")


def save_file():
    return asksaveasfile(mode='w', confirmoverwrite=True, defaultextension='png', initialfile="watermarked_image.png")


window = Tk()
window.title("Watermarker")
window.config()

# Logo section
canvas = Canvas(width=500, height=100, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 50, image=logo_img)
canvas.pack()

# Load image section
load_title = Label(text="Choose Image")
load_title.pack()
load_button = Button(text="Open", command=open_file)
load_button.pack()

# Save image section
save_title = Label(text="Save")
save_title.pack()
save_button = Button(text="Save", command=save_file)
save_button.pack()

wtrmrk = Image.open("watermark.png")
im = Image.open("user_image.png")

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

window.mainloop()


# TODO 1. Figure out how to load images (save in directory), process image with watermark, save edited images after
