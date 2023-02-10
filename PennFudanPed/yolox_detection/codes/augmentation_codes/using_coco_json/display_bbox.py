#DISPLAYING THE BBOX ON THE IMAGES GIVEN GROUNDTRUTH LABELS

from PIL import Image
import PATHS as PATHS
import json
import cv2
import os


"""
COCO : [x_top_left, y_top_left, width, height]
PASCAL VOC : [x_top_left, y_top_left, x_bottom_right, y_bottom_right]
"""
#Path to the Json annotation file 
"""
NOTE: The JSON Annotation File contains the annotations of all the images mentioned in the list.txt 
and not just one detection.
"""
ANNOT_PATH = "/Users/sankeerthana/Documents/NTU/YEAR_4/FYP/fyp-pedestrian-detection/PennFudanPed/yolox_detection/codes/augmentation_codes/json_annot/annots.json"

#Opening and reading the json annotations file
f = open(ANNOT_PATH)
contents = json.load(f)

#Getting only the values of the key 'annotations'
annots = contents['annotations'] #big list
annots_info = {}

#Sorting the annotations according to the image id
for d in annots:
    annots_info[d['image_id']] = []

#Helper fxn - adding boxes to the new dctionary according to the image id
def add_bbox(img_name):
    for b in annots:
        if b['image_id'] == img_name:
            annots_info[img_name].append(b['bbox'])
               
for name in list(annots_info.keys()):
    add_bbox(name)


#Iterating through all the image id and drawing the respective predictions for that image
for img in list(annots_info.keys()):
    IMG_PATH = os.path.join(PATHS.IMAGES, str(img+'.jpg'))

    image = cv2.imread(IMG_PATH)

    for box in annots_info[img]:

        tl_x = box[0]
        tl_y = box[1]

        br_x = tl_x + box[2]
        br_y = tl_y + box[3]

        top_left = (tl_x, tl_y)
        bottom_right = (br_x, br_y)

        colour = (0,0,255)
        thickness = 1

        img = cv2.rectangle(image, top_left, bottom_right, colour, thickness)
        image = img
    cv2.imshow('try2', img)
    #cv2.waitKey(0)
        

