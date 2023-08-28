from PIL import Image

import pytesseract

# Path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open image
file = Image.open('C:\\Users\\Julian\\Documents\\Proyectos\\Inteligencia-Artificial\\ocr-test\\test-teso.png')


txt = pytesseract.image_to_string(file)
print(txt)

# List of available languages
#print(pytesseract.get_languages(config=''))

