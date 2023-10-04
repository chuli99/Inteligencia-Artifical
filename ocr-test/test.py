import cv2
import numpy as np
import pytesseract
import filter 


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\nombre.jpg')


gray = filter.get_grayscale(img)
thresh = filter.thresholding(gray)
opening = filter.opening(gray)
canny = filter.canny(gray)

txt = pytesseract.image_to_string(img, config='--psm 6', nice=0, output_type=pytesseract.Output.STRING)
print(txt)
