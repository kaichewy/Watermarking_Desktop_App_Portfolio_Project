from tkinter import *
from tkinter import ttk, filedialog
import os
from PIL import Image, ImageTk, ImageEnhance
from water_marker import WaterMarker

filepath1 = None
filepath2 = None

# Functions
def openfolder():
    global original_image
    global filepath1
    file = filedialog.askopenfile(mode='r')
    if file:
        filepath1 = os.path.abspath(file.name)
        # load image to be "edited"
        image = PhotoImage(file=filepath1)
        original_image = image.subsample(3, 3)  # resize image using subsample
        Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)


def openfolder2():
    global water_marked_image
    global filepath2
    file = filedialog.askopenfile(mode='r')
    if file:
        if filepath1:
            filepath2 = os.path.abspath(file.name)

            water_marked_image = WaterMarker(filepath1, filepath2)
            print(filepath1)
            print(filepath2)
            water_marked_image = water_marked_image.create_watermarked_image()
            water_marked_image = ImageTk.PhotoImage(water_marked_image)
            Label(right_frame, image=water_marked_image).grid(row=0, column=0, padx=5, pady=5)
        else:
            Label(right_frame, text="SELECT IMAGE FIRST").grid(row=0, column=0, padx=5, pady=5)

# Create window
window = Tk()
window.title("Water Marking App")
window.maxsize(900, 600)  # specify the max size the window can expand to
window.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(window, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(window, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)


# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu
Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

# Buttons
image_button = Button(text="Select Watermark", highlightthickness=0, font=("Courier", 20, "bold"), command=openfolder2)
image_button.grid(column=0, row=2)
image_button = Button(text="Select Image", highlightthickness=0, font=("Courier", 20, "bold"), command=openfolder)
image_button.grid(column=0, row=1)


window.mainloop()
