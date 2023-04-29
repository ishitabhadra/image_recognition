from PIL import Image
from pytesseract import *
import numpy as np

filename = input("please enter a file name:  ")
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)
