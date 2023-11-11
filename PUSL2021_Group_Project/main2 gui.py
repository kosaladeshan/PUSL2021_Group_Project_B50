import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Button Interface")

# Function to handle button clicks
def button_click(button_number):
    print(f"Button {button_number} clicked!")

# Create and add images to buttons
button_images = []
for i in range(1, 7):
    button = tk.Button(root, text=f"Button {i}", width=20, height=10, command=lambda i=i: button_click(i))
    button.grid(row=i//2, column=i%2)
    button_images.append(button)

# Load and add images at the bottom with error handling
try:
    image1 = Image.open("image1.png")  # Replace with the actual image path
    image1 = image1.resize((400, 200))  # Adjust the dimensions as needed
    photo1 = ImageTk.PhotoImage(image1)
    image_label1 = tk.Label(root, image=photo1)
    image_label1.grid(row=3, column=0, columnspan=2)
except FileNotFoundError:
    print("Image1 not found. Please provide the correct path.")

try:
    image2 = Image.open("image2.png")  # Replace with the actual image path
    image2 = image2.resize((400, 200))  # Adjust the dimensions as needed
    photo2 = ImageTk.PhotoImage(image2)
    image_label2 = tk.Label(root, image=photo2)
    image_label2.grid(row=4, column=0, columnspan=2)
except FileNotFoundError:
    print("Image2 not found. Please provide the correct path.")

# Start the Tkinter main loop
root.mainloop()
