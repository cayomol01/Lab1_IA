from PIL import Image
import numpy as np


# Open the image
tur = Image.open("turing.png")
la = Image.open("lab1.bmp")

TURING = 4
LAB = 20

outTur = "pruebaa.bmp"
outLab = "prueba.bmp"
count = 0

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
    
print(count)
cambiar(tur, TURING, outTur)
resize(la, LAB, "probando.bmp")
resize(tur, TURING, "resize_tur.bmp")
#cambiar(la, LAB, outLab)