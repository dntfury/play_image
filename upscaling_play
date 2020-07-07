#upscale image
#rescale and operations over the pixels
#SOR algo try
#doulbe the number of row and Column
from PIL import Image
import numpy as np
from scipy import misc


def open_image(name):
    image=Image.open(name)
    print(image.format, image.size, image.mode)
    return image
    """
#attributes to examine the image

#formate=

#size=width and height (in pixels)

# modes= defines the number and names of the bands in the image,
#and also the pixel type and depth.
#Common modes are “L” (luminance) for greyscale images,
#“RGB” for true color images,
#and “CMYK” for pre-press images.

    """

def image_to_array(img):
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data


def array2image(a):
    Image.fromarray(a, mode='RGB').save('d1.png')
        
image1=open_image("d.jpg")
#image2=open_image("3.jpg")
data1=image_to_array(image1)
#data2=image_to_array(image1)

width,height=image1.size

for i in range(0,250):
    for j in range(0,230):
        for k in range(0,3):
            data1[i][j][k] = int(data1[i][j][k]/4)

#width,height=data1.size
print(data1.size)
print(data1.shape)
#print(data2.size)
#print(data2.shape)

#array2image(data1)
#print("done1")

from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
plt.imshow(data1, interpolation='nearest')
plt.show()




