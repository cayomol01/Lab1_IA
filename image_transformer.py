from PIL import Image
import numpy as np


# Open the image
tur = Image.open("img/turing.png")
la = Image.open("img/lab1.bmp")

TURING = 4
LAB = 20

outTur = "img/pruebaa.bmp"
outLab = "img/prueba.bmp"

# Resize the image to a smaller size

def cambiar(image, size,out):
    small_image = image.resize((int(image.width / size), int(image.height / size)))

    # Resize the smaller image back to its original size
    pixelated_image = small_image.resize((image.width, image.height), Image.NEAREST)
    pixelated_image.save(out)

def resize(image, size, out):
    small_image = image.resize((int(image.width / size), int(image.height / size)))
    print(image.width / size, image.height/size)

    small_image.save(out)
    
cambiar(tur, TURING, outTur)
resize(la, LAB, "img/probando.bmp")
resize(tur, TURING, "img/resize_tur.bmp")
#cambiar(la, LAB, outLab)