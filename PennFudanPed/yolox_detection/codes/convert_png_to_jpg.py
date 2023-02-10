#CODE TO CONVERT .PNG IMAGES TO .JPG

from PIL import Image
import os

PARENT = "/Users/sankeerthana/Documents/NTU/YEAR_4/FYP/fyp-pedestrian-detection/PennFudanPed/"

contents = os.listdir(os.path.join(PARENT, 'PNGImages'))

os.chdir('yolox_detection')

for img in contents:
    img1 = Image.open(os.path.join(PARENT,'PNGImages', img))
    img_jpg = img[:-4] + '.jpg'
    jpg_path = os.path.join(PARENT, 'yolox_detection','images',img_jpg)
    img1.save(jpg_path)





    



