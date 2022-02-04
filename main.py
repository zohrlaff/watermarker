from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image


# TODO 1. Document, Refactor, Tweak
# TODO 2. Let user choose an image for watermarking

def open_file():
    """

    :return:
    """

    global image_blend

    # Capture file path for the user's choice
    file_name = askopenfilename(title="Select an image", initialdir="C:\\",
                                filetypes=[("All Files", "*.*"), ("Image Files", "*.png")])

    # Location/name of image to be used as watermark
    watermark = Image.open("watermark.png")
    # User's chosen image object generation
    im = Image.open(file_name)

    # Image size unpacking
    x_size, y_size = im.size

    # Locations for watermark
    # TODO 3. Make all of this trash below cleaner vvvvvvvvv
    watermark_grid = []
    x_center, y_center = (x_size // 2 - 100), (y_size // 2)
    top_left = (x_size // 4 - 100, y_size // 4)
    top_right = (round(x_size * .75 - 100), y_size // 4)
    bottom_left = (x_size // 4 - 100, round(y_size * .75))
    bottom_right = (round(x_size * .75 - 100), round(y_size * .75))

    # Creation of blank placeholder images
    placeholder_image = Image.new("RGBA", im.size, (255, 255, 255, 0))
    watermark_layer = Image.new("RGBA", im.size, (255, 255, 255, 1))

    # Paste user's image to blank canvas
    placeholder_image.paste(im=im)

    # Add watermarks to user's image
    watermark_layer.paste(im=watermark, box=(x_center, y_center), mask=watermark)
    watermark_layer.paste(im=watermark, box=top_left, mask=watermark)
    watermark_layer.paste(im=watermark, box=top_right, mask=watermark)
    watermark_layer.paste(im=watermark, box=bottom_left, mask=watermark)
    watermark_layer.paste(im=watermark, box=bottom_right, mask=watermark)

    # Blend both images for 'watermarked' result
    image_blend = Image.blend(placeholder_image, watermark_layer, .1)
    # Save image to local directory
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
