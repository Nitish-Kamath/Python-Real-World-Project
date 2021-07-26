# OCR stands for "Optical Character Recognition." 
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"   #path to tesseract
def convert():
    img=Image.open('images.png')
    text=pytesseract.image_to_string(img)
    print(text)
convert()