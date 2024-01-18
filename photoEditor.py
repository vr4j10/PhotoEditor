import os
import uuid
from PIL import Image, ImageFilter, ImageEnhance
from tkinter import Tk, filedialog


current_working_directory = os.getcwd() # Current working directory

def apply_gaussian_blur(img):
    # Apply a Gaussian blur filter
    return img.filter(ImageFilter.GaussianBlur(radius=2))

def apply_image_sharpness(img):
    # Apply a SHARPEN filter
    return img.filter(ImageFilter.SHARPEN)

def enhance_brightness(img):
    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(1.5)  # Increase brightness by 50%

def enhance_contrast(img):
    # Enhance Contrast
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(1.5) # Increase contrast by 50%

def process_image(input_path, output_folder):

    img = Image.open(input_path) # Open an image

    # Apply a Gaussian blur
    blurred_img = apply_gaussian_blur(img)

    # Enhance brightness
    brightened_img = enhance_brightness(blurred_img)

    # Generate a unique identifier
    unique_id = str(uuid.uuid4().hex)[:8]  # Use the first 8 characters of the UUID

    # Create the output file name with "edited" and the unique identifier
    output_filename = f"edited_{unique_id}.png"
    
    # Save the result in the specified folder with the unique filename
    output_path = os.path.join(output_folder, output_filename)
    brightened_img.save(output_path)

    # Show the original and processed images
    img.show(title="Original Image")
    brightened_img.show(title="Processed Image")

def choose_file():
    # Creates a Tkinter root window
    root = Tk()
    root.withdraw()

    # Prompts the user to choose a file
    image_path = filedialog.askopenfilename(initialdir=current_working_directory, title="Select an Image")

    # Check if the user selected a file
    if image_path:
        print("Selected File:", image_path)
        return image_path
    else:
        print("No file selected.")
        return None
    
def choose_folder():
    # Prompts the user to choose a file
    folder_path = filedialog.askdirectory(title="save as")

    # Check if the user selected a file
    if folder_path:
        return folder_path
    else:
        print("No file selected.")
        return None

input_image_path = choose_file()

if input_image_path:
    output_image_path = choose_folder()  # output path

    if output_image_path:
        process_image(input_image_path, output_image_path)
