from PIL import Image

# Load the image from a file named 'image.png'
img = Image.open('code.png')

# Save the loaded image in WebP format with the filename 'output_image.webp'
img.save('output_image.webp', 'WEBP')

# Print a confirmation message to the console
print("Image saved in WebP format.")