from PIL import Image
import numpy as np
from graph_search import GraphSearch

TURING = "img/pruebaa.bmp"
outTuring = "img/new_turing.bmp"

LAB  = "img/prueba.bmp"
outLab = "img/new_lab.bmp"

test = "img/probando.bmp"
test1 = "probando1.bmp"


def normal(imagen, output):
    img = Image.open(imagen)

    colors = [(255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)]

    # Create a new image with the same size as the original image
    new_img = Image.new("RGB", img.size)

    # Iterate over each pixel in the original image
    for x in range(img.width):
        for y in range(img.height):
            # Get the RGB values of the current pixel
            r, g, b = img.getpixel((x, y))
            
            
            # Find the closest color in the list of desired colors
            closest_color = min(colors, key=lambda color: sum([(r - color[0]) ** 2, (g - color[1]) ** 2, (b - color[2]) ** 2]))
            
            limit = 100
            if closest_color!=colors[-1]:
                if r<=limit and g<=limit and b <=limit:
                    closest_color = colors[1]
                elif r>limit and g>limit and b >limit:
                    closest_color = colors[0]
            
            # Set the corresponding pixel in the new image to the closest color

            new_img.putpixel((x, y), closest_color)
                

    # Save the new image
    new_img.save(output)

imagen = Image.open("img/probando1.bmp")
img_array = np.array(imagen)
print(len(img_array[0]))

normal(TURING, outTuring)
normal(test, test1)

hola = GraphSearch(1, imagen)
hola.Search()


normal("img/resize_tur.bmp", "img/resize_tur_test.bmp")
#normal(LAB, outLab)