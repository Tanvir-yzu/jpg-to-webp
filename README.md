```markdown:README.md
# Image Format Converter

This simple Python script uses the PIL (Python Imaging Library) library to convert an image from PNG format to WebP format.

## Requirements

To run this script, you need Python installed on your system along with the PIL library. You can install PIL (now known as Pillow) using pip:

```bash
pip install Pillow
```

## Usage

1. Place the image you want to convert into the same directory as the script. The current script expects an image named `code.png`.
2. Run the script using Python:

```bash
python main.py
```

3. After successful execution, the script will save the converted image in WebP format as `output_image.webp` in the same directory and print a confirmation message to the console.

## Note

- The script currently only converts from PNG to WebP format. For converting different formats, you can modify the `Image.open('code.png')` and `img.save('output_image.webp', 'WEBP')` lines in the `main.py` file accordingly.
- Ensure you have the necessary permissions to read and write files in the script's directory.
```