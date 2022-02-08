import random
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageDraw, ImageFont


# TODO 1. Document

def load_file():
    """

    :return:
    """

    # Capture file path for the user's choice
    file_name = askopenfilename(title="Select an image", initialdir="C:\\",
                                filetypes=[("All Files", "*.*"), ("Image Files", "*.png")])
    #
    im = Image.open(file_name)
    im.save("user_file.png")


def edit_file():
    """

    :return:
    """

    # User's chosen image object generation
    im = Image.open("user_file.png")

    # Watermark text creation
    # Layer for watermark text
    watermark_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))
    # Capture text from GUI Entry widget and define font
    watermark_text = watermark_var.get()
    watermark_font = ImageFont.truetype("arial.ttf", 24)

    # Draw object for watermark text
    draw_text = ImageDraw.Draw(watermark_layer)

    # Image size unpacking
    x_size, y_size = im.size

    # Margins/limits for watermarks
    y_margin_min, y_margin_max = (int(y_size * .5), int(y_size - y_size * .5))
    x_margin_min, x_margin_max = (int(x_size * .10), int(x_size - x_size * .10))

    # Watermark locations
    y_range = []
    for r in range(0, y_size, y_size // 8):
        y_range.append(r)

    for i in range(8):
        x = random.randint(x_margin_min, x_margin_max)
        draw_text.text((x, y_range[i]), watermark_text, fill=(233, 233, 233, 125), font=watermark_font)

    # Blank user image sized layer to copy image to
    image_copy = Image.new("RGBA", im.size, (255, 255, 255, 0))
    image_copy.paste(im=im)

    # Blend watermark layer and user image, save locally
    image_blend = Image.alpha_composite(image_copy, watermark_layer)
    image_blend.save("watermarked_image.png")


def save_file():
    """

    :return:
    """

    watermarked_image_location = asksaveasfilename(title="Save watermarked image", confirmoverwrite=True,
                                                   defaultextension=".png",
                                                   initialfile="watermarked_image.png", initialdir="C:\\",
                                                   filetypes=[("PNG File", "*.png"), ("JPG File", "*.jpg"),
                                                              ("BMP File", "*.bmp"),
                                                              ("All Files", "*.*")])
    im = Image.open("watermarked_image.png")
    im.save(watermarked_image_location)


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
load_button = Button(text="Open", command=load_file)
load_button.pack()

# Watermark text entry
watermark_label = Label(text="Watermark Text")
watermark_label.pack()

watermark_var = StringVar()
watermark_user_text = Entry(textvariable=watermark_var)
watermark_select = Button(text="Select", command=edit_file)
watermark_user_text.pack()
watermark_select.pack()

# Save image section
save_title = Label(text="Save")
save_title.pack()
save_button = Button(text="Save", command=save_file)
save_button.pack()

window.mainloop()
