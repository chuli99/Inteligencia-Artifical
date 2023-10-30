from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import cv2
import pytesseract
import pandas as pd
import os
from deep_translator import GoogleTranslator


class OCR():
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dani_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        self.path_output = 'ocr_2023_um/output/'
        self.path_images = 'ocr_2023_um/imagenes/'
        self.processor = TrOCRProcessor.from_pretrained(
            "microsoft/trocr-base-handwritten")
        self.model = VisionEncoderDecoderModel.from_pretrained(
            "microsoft/trocr-base-handwritten")

    def clear_output(self):
        for f in os.listdir(self.path_output):
            os.remove(os.path.join(self.path_output, f))

    def load_image(self, image):
        return cv2.imread(self.path_images + image)

    def filter(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def data_frame(self, gray):
        return pytesseract.image_to_data(
            gray, lang="spa", config="--psm 12",
            output_type=pytesseract.Output.DATAFRAME)

    def crop_image(self, df, gray):
        line_start = None
        count = 0
        for index, row in df.iterrows():
            if not pd.isna(row["text"]):
                if line_start is None:
                    line_start = index
            else:
                if line_start is not None:
                    x, y, w, h = df.loc[line_start, "left"], df.loc[line_start, "top"], \
                        df.loc[index - 1, "width"] + df.loc[index - 1, "left"] - df.loc[line_start, "left"], \
                        df.loc[index - 1, "height"] + \
                        df.loc[index - 1, "top"] - \
                        df.loc[line_start, "top"]
                    cropped_image = gray[y:y+h, x:x+w]
                    cv2.imwrite(
                        f"ocr_2023_um/output/linea_{count}.png", cropped_image)
                    count += 1

                line_start = None
        if line_start is not None:
            x, y, w, h = df.loc[line_start, "left"], df.loc[line_start, "top"], \
                df.loc[index, "width"] + df.loc[index, "left"] - df.loc[line_start, "left"], \
                df.loc[index, "height"] + df.loc[index,
                                                 "top"] - df.loc[line_start, "top"]
            cropped_image = gray[y:y+h, x:x+w]
            cv2.imwrite(f"ocr_2023_um/output/linea_{count}.png", cropped_image)

    def image_to_text(self, image):
        text = ''
        for file in os.listdir('ocr_2023_um/output/'):
            image = Image.open('ocr_2023_um/output/'+file).convert("RGB")

            pixel_values = self.processor(
                image, return_tensors="pt").pixel_values
            generated_ids = self.model.generate(
                pixel_values, max_new_tokens=10000)

            generated_text = self.processor.batch_decode(
                generated_ids, skip_special_tokens=True)[0]
            text += generated_text + "\n"
        return text

    def translate(self, text):
        return GoogleTranslator(source='en', target='es').translate(text)

    def main(self):
        while True:
            os.system('cls')
            count = 1
            print("########## Imagenes ##########")
            files = []
            for file in os.listdir(self.path_images):
                print(str(count) + " - " + file)
                files.append(file)
                count += 1
            image = input("-> ")
            os.system('cls')
            print("Procesando...")
            self.clear_output()
            image = self.load_image(files[int(image)-1])
            gray = self.filter(image)
            df = self.data_frame(gray)
            self.crop_image(df, gray)
            text = self.image_to_text(image)
            text = self.translate(text)
            os.system('cls')
            print("########## Resultado ##########\n\n" + text)
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    ocr = OCR()
    ocr.main()
