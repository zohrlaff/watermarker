from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image

# TODO 1. Document, Refactor, Tweak

def open_file():
    global image_blend

    # Capture file path
    file_name = askopenfilename(title="Select an image", initialdir="C:\\",
                                filetypes=[("All Files", "*.*"), ("Image Files", "*.png")])

    wtrmrk = Image.open("watermark.png")
    im = Image.open(file_name)

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

    image_blend = Image.blend(canvas, watermark_layer, .2)
    # image_blend.show()

    image_blend.save("watermarked_image.png")


def save_file():
    watermarked_image = asksaveasfilename(title="Save watermarked image", confirmoverwrite=True,
                                          defaultextension=".png",
                                          initialfile="watermarked_image.png", initialdir="C:\\",
                                          filetypes=[("PNG File", "*.png"), ("JPG File", "*.jpg"),
                                                     ("BMP File", "*.bmp"),
                                                     ("All Files", "*.*")])
    image_blend.save(f"{watermarked_image}")


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

window.mainloop()
