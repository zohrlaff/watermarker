from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

def open_file():
    return askopenfile(mode='r', filetypes=[('Image Files', '*.png'), ('All Files', '*.*')])


def save_file():
    return asksaveasfile(mode='w', confirmoverwrite=True, defaultextension='.png', initialfile="/watermarked_image.png")


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
load_button = Button(text="Open", command=main.open_file)
load_button.pack()

# Save image section
save_title = Label(text="Save")
save_title.pack()
save_button = Button(text="Save", command=main.save_file)
save_button.pack()

window.mainloop()
