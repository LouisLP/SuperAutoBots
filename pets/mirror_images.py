from PIL import Image
import os

def reflect_image_horizontally(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Reflect the image
    img_reflected = img.transpose(Image.FLIP_LEFT_RIGHT)
    # Save the reflected image
    img_reflected.save(os.path.basename(image_path))

# Directory with images
image_dir = 'original_images'

# Get a list of all image files in the directory
image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg'))]

# Reflect all images
for image_path in image_paths:
    reflect_image_horizontally(image_path)