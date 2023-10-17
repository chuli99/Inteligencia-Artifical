import cv2
import numpy as np
import pytesseract
import filter 


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\texto-manuscrito.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('Original', img)

_, result = cv2.threshold(img, 100,255, cv2.THRESH_BINARY, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
#cv2.imshow('Threshold', result)
cv2.waitKey(0)

print("Aplicando filtrado...")
gray = filter.get_grayscale(img)
thresh = filter.thresholding(gray)
opening = filter.opening(gray)
canny = filter.canny(gray)

print("Aplicando OCR...")
txt = pytesseract.image_to_string(result, config='--psm 6 --oem 3 -l spa', nice=0, output_type=pytesseract.Output.STRING)
print("Texto:")
print(txt)
