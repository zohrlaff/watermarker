import random
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageDraw, ImageFont
import os


# TODO 2. Document

def load_file():
    """
    Loads file for manipulation. File is saved as 'user_file.png' by default in local program directory.
    """

    # Capture file path for the user's choice
    file_name = askopenfilename(title="Select an image", initialdir="C:\\",
                                filetypes=[("Image Files", ["*.png", "*.jpg", "*.jpeg"]), ("All Files", "*.*")])
    #
    im = Image.open(file_name)
    im.save("user_file.png")


def edit_file():
    """
    Manipulates image selected by user for watermarking.

    An empty canvas layer is created, the user's chosen text is captured, the dimensions of the user image are
    calculated and boundaries are set, the image is divided to create the plot points for each watermark,
    each watermark is drawn on the previously empty canvas layer, and finally both layers are combined into one.
    """

    # User's chosen image object generation
    im = Image.open("user_file.png")

    # --- Watermark text creation ---#
    # Layer for watermark text
    watermark_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))
    # Capture text from GUI Entry widget and define font
    watermark_text = watermark_var.get()
    watermark_font = ImageFont.truetype("calibri.ttf", 40)

    # Draw object for watermark text
    draw_text = ImageDraw.Draw(watermark_layer)

    # Image size unpacking
    x_size, y_size = im.size

    # Margins/limits for watermarks
    y_margin_min, y_margin_max = (int(y_size * .10), int(y_size - (y_size * .05)))
    x_margin_min, x_margin_max = (int(x_size * .05), int(x_size - (x_size * .05)))

    # Locations for watermarks
    y_range = [y_plot for y_plot in range(y_margin_min, y_margin_max, y_size // 12)]
    x_range = [x_plot for x_plot in range(x_margin_min, x_margin_max, x_size // 12)]

    # Image 'stamping' with watermarks
    for r in range(len(y_range)):
        x = random.choice(x_range)
        draw_text.text((x, y_range[r]), watermark_text, fill=(230, 230, 230, 128), font=watermark_font)
        x_range.pop(x_range.index(x))

    # Blank user-image-sized layer to copy image to
    image_copy = Image.new("RGBA", im.size, (255, 255, 255, 0))
    image_copy.paste(im=im)

    # Blend watermark layer and user image, and save locally
    image_blend = Image.alpha_composite(image_copy, watermark_layer)
    image_blend.save("watermarked_image.png")


def save_file():
    """
    Watermarked image is saved to the user's location of choice.
    """

    watermarked_image_location = asksaveasfilename(title="Save watermarked image", confirmoverwrite=True,
                                                   defaultextension=".png",
                                                   initialfile="watermarked_image.png", initialdir="C:\\",
                                                   filetypes=[("PNG File", "*.png"), ("JPG File", "*.jpg"),
                                                              ("BMP File", "*.bmp"),
                                                              ("All Files", "*.*")])
    im = Image.open("watermarked_image.png")
    im.save(watermarked_image_location)


# --- GUI Section ---#

window = Tk()
window.title("Image Watermarker v1.0")

big_frame = ttk.Frame(window)
big_frame.pack(fill="both", expand=True)

# GUI Theme settings
window.tk.call("source", "sun-valley.tcl")
window.tk.call("set_theme", "light")

# Logo section
canvas = Canvas(width=500, height=100)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 50, image=logo_img)
canvas.pack()

# Load image section
load_button = ttk.Button(text="Choose Image", command=load_file)
load_button.pack(pady=(0, 15))

# Watermark text entry
watermark_label = Label(text="Watermark Text")
watermark_label.pack()

watermark_var = StringVar()
watermark_user_text = ttk.Entry(textvariable=watermark_var)
watermark_select = ttk.Button(text="Stamp Text", command=edit_file)
watermark_user_text.pack()
watermark_select.pack(pady=(0, 15))

# Save image section
save_button = ttk.Button(text="Save Watermarked Image", command=save_file)
save_button.pack(pady=(0, 15))

window.mainloop()

# Delete locally saved files after program closes
os.remove("user_file.png")
os.remove("watermarked_image.png")
