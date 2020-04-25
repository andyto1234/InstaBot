import numpy as np
from PIL import Image, ImageEnhance, ImageDraw

image = Image.open("/Users/ato/Desktop/Screenshot 2020-04-08 at 11.04.13.png")
b = (10,30, 220, 200)
image = image.crop(box=b)
im = ImageEnhance.Contrast(image)
image=im.enhance(1.1)

image_data = np.asarray(image)
image_data_blue = image_data[:,:,0]
image_data_blue = image_data[image_data_blue>200]


non_empty_columns = np.where(image_data_blue(axis=0)>200)[0]
non_empty_rows = np.where(image_data_blue(axis=1)>200)[0]
draw = ImageDraw.Draw(image)
for i in image_data_blue:
    box = [i[0]-5, i[1]+5, i[2]-5, i[3]+5]
    draw.ellipse(box, fill='blue', outline='blue')

image.show()
# draw.ellipse((20, 20, 180, 180), fill = 'blue', outline ='blue')
# boundingBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
#
# print boundingBox