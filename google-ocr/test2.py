import numpy as np
import cv2
import math
import numpy as np
from deskew import determine_skew
import pytesseract

from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate

from deskew import determine_skew

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def deskew_process(img):
	image = cv2.imread(img)
	grayscale = filter.rgb2gray(image)
	angle = determine_skew(grayscale)
	rotated = rotate(image, angle, resize=True) * 255
	return rotated

#image_deskew = deskew_process(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\texto-manuscrito.jpg')
#save the rotated image to a imagae .png file
output = io.imread(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\google-ocr\Images\arquitectura.jpg')
io.imsave('output.png', output.astype(np.uint8))




def pre_process_image(image):
    """This function will pre-process a image with: cv2 & deskew
    so it can be process by tesseract"""
    img = cv2.imread(image)
    img = cv2.resize(img, None, fx=.3, fy=.3) #resize using percentage
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #change color format from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #format image to gray scale
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 11) #to remove background
    return img

#pass the deskew image
processed_img = pre_process_image(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\arquitectura.jpg')
#save the processed image to a imagae .png file
cv2.imwrite("output_processed.png",processed_img)

txt = pytesseract.image_to_string(processed_img, config='--psm 6', nice=0, output_type=pytesseract.Output.STRING)
print("Texto:")
print(txt)
