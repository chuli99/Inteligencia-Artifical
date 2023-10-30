import cv2
import numpy as np
import pytesseract
import filter 
import bardApi

class PYTESSERACT():
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def open_image(self, path):
        img = cv2.imread(path)
        return img
    
    def process_image(self, img):
        _, result = cv2.threshold(img, 100,255, cv2.THRESH_BINARY, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        cv2.waitKey(0)
        gray = filter.get_grayscale(result)
        cv2.imwrite("result.jpg", gray)
        return gray
    
    def get_text(self,img):
        txt = pytesseract.image_to_string(img, config='--psm 11', nice=0, output_type=pytesseract.Output.STRING )
        return txt
    
    def fix_text(self,txt):
        correctedText = bardApi.get_response(txt)
        print("Texto corregido:\n")
        print(correctedText)
        
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    def main(self):
        imagen = self.open_image(r'C:\Users\Julian\Documents\Proyectos\Inteligencia-Artifical\ocr-test\Img\poema.jpg')
        imagenProcesada = self.process_image(imagen)
        texto = self.get_text(imagenProcesada)
        print(texto)
        #self.fix_text(texto)

if __name__ == "__main__":
    test = PYTESSERACT()
    test.main()






    

