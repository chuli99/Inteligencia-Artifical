from PIL import Image

import pytesseract
import cv2 
import numpy as nps

# Path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open image
file = Image.open(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\nombre.jpg')

txt = pytesseract.image_to_string(file, config='--psm 6', nice=0, output_type=pytesseract.Output.STRING )
print(txt)


