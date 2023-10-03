from detect_aruco_images import detect#

import tkinter as tk
from tkinter import filedialog


if __name__ == "__main__":
    types = {1 : "DICT_4X4_100",
             2 : "DICT_4X4_250",
             3 : "DICT_5X5_100",
             4 : "DICT_5X5_250"}
    
    print(types)
    input = input("Please Enter an exact type number (e.g 1, 2 etc)")

    type = types.get(int(input))

    print(f"You have chosen: {type}")

    root = tk.Tk()
    root.withdraw()

    image_input = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm")]
    )

    if not image_input:
        print("No image file selected. Exiting.")
    else:
        print(f"Selected image file: {image_input}")
    
    detect(image_input, type)

