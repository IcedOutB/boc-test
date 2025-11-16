from PIL import Image, ImageOps
import os

def resize_and_pad(image_path, scale_factor=0.6653):
    with Image.open(image_path) as img:
        original_width, original_height = img.size
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        # Resize image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Create a new image with original dimensions and transparent background
        new_img = Image.new("RGBA", (original_width, original_height), (0, 0, 0, 0))

        # Paste the resized image onto the new image, centered
        paste_position = (
            (original_width - new_width) // 2,
            (original_height - new_height) // 2
        )
        new_img.paste(resized_img, paste_position)

        # Convert back to original mode (e.g., RGB)
        if img.mode != 'RGBA':
            new_img = new_img.convert(img.mode)

        # Save the new image, overwriting the original
        new_img.save(image_path)

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
            image_path = os.path.join(folder_path, filename)
            resize_and_pad(image_path)

if __name__ == "__main__":
    folder_path = os.getcwd()
    process_images_in_folder(folder_path)
