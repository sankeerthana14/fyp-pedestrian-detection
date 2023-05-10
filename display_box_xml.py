#READING FROM XML FILES AND DISPLAYING BBOX

from xml.dom import minidom
import cv2
import os

#reading from each xml file
def read_xml(FILE_PATH):
    annot_info = {}

    file = minidom.parse(FILE_PATH)
    xmin = file.getElementsByTagName('xmin')
    ymin = file.getElementsByTagName('ymin')
    xmax = file.getElementsByTagName('xmax')
    ymax = file.getElementsByTagName('ymax')
    filename = file.getElementsByTagName('filename')


    order = {0:xmin, 1:ymin, 2:xmax, 3:ymax}

    for i in range(4):
        counter = 0
        for element in order[i]:
            if i == 0:
                annot_info[counter] = []
            annot_info[counter].append(int(element.firstChild.data))
            counter += 1

    return annot_info

annot_info = read_xml("/Users/sankeerthana/Documents/NTU/YEAR_4/FYP/fyp-pedestrian-detection/PennFudanPed/yolox_detection/annotations/FudanPed00002.xml")
"""
»» Format : [xmin, ymin, xmax, ymax]

»» Bounding Box Coordinates:
    • Top Left Corner - (xmin, ymin)
    • Bottom Right Corner - (xmax, ymax)
    • Top Right Corner - (xmax, ymin)
    • Bottom Left Corner - (xmin, ymax)
"""
#hard coding it right now, later can make it dynamic -> all the annotations in one pictue in 1 list
info = [annot_info[0], annot_info[1]]


def display_box(IMG_PATH, info):
    #reading the image
    image = cv2.imread(IMG_PATH)

    #iterating through all the annotations in 1 picture and displaying it
    for box in info:
        top_left = (box[0], box[1])
        bottom_right = (box[2], box[3])

        colour = (0,0,255)
        thickness = 1

        img = cv2.rectangle(image, top_left, bottom_right, colour, thickness)
        image = img
    cv2.imshow('try2', img)
    cv2.waitKey(0)


def calc_iou(bbox1, bbox2):
    #Calculating measures of the 2 bounding boxes
    width1 = bbox1[2] - bbox1[0]
    width2 = bbox2[2] - bbox2[0]

    height1 = bbox1[3] - bbox1[1]
    height2 = bbox2[3] - bbox2[1]

    box_area1 = width1 * height1
    box_area2 = width2 * height2

    #calculating the intersection coordinates
    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[2], bbox2[2])
    y_bottom = min(bbox1[3], bbox2[3])

    """
    »» Intersection Area Coordinates:
        • Top Left Corner - (x_left, y_top)
        • Bottom Right Corner - (x_right, y_bottom)
        • Top Right Corner - (x_right, y_top)
        • Bottom Left Corner - (x_left, y_bottom)
    """

    #If there is no overlap then return 0
    if x_right < x_left or y_bottom < y_top:
        x_left, y_top, x_right, y_bottom, IoU = 0,0,0,0,0

    #Calculating the intersection area
    intersection_width = x_right - x_left
    intersection_height = y_bottom - y_top

    intersection_area = intersection_width * intersection_height

    #Calculating the Union area
    union_area = box_area1 + box_area2 - intersection_area

    #Calculating IoU
    IoU = intersection_area / union_area

    return [x_left, y_top, x_right, y_bottom, IoU]

#print(calc_iou(annot_info[0], annot_info[1]))