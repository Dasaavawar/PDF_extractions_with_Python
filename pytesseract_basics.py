import pdf2image
import pytesseract
from pytesseract import Output, TesseractError

pdf_path = '/home/user/Desktop/file.pdf'

images = pdf2image.convert_from_path(pdf_path)

text = ""
# to extract the text from all pages
for i in range(0, len(images)):
    pil_im = images[i]
    # ocr_dict now holds all the OCR info including text and location on the image
    ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
    text += " ".join(ocr_dict['text'])

print(text)

