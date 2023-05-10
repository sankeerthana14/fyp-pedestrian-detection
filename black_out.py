#GREYING OUT THE INTERSECTION AREA
import HELPER as HELPER
import numpy as np
import cv2
import os

def black_out(IMAGE_PATH, x_left, y_top, x_right, y_bottom, counter):
    image = cv2.imread(IMAGE_PATH)

    #intersection coordinates
    #x_left = 126
    #y_top = 98
    #x_right = 192
    #y_bottom = 373

    """
    »» Intersection Area Coordinates:
        • Top Left Corner - (x_left, y_top)
        • Bottom Right Corner - (x_right, y_bottom)
        • Top Right Corner - (x_right, y_top)
        • Bottom Left Corner - (x_left, y_bottom)
    """

    # Define a black  mask
    mask = np.zeros_like(image)
    #Flip the mask color to white
    mask[:, :] = [255, 255, 255] 

    #Draw a black filled rectangle on top of the mask to hide a specific area
    start_point = (x_left, y_top)
    end_point = (x_right, y_bottom)
    color = (0,0,0)
    mask = cv2.rectangle(mask, start_point, end_point, color, -1)

    #mask = 1 - mask
    # Apply the mask to image
    result = cv2.bitwise_and(image,mask)

    cv2.imshow('try2', result)
    cv2.waitKey(0)
    
    file_path = get_aug_img_name(counter, IMAGE_PATH)
    cv2.imwrite(file_path, result)


def get_aug_img_name(counter, IMG_PATH):
    dir, file = os.path.split(IMG_PATH)
    file_path = os.path.join(HELPER.AUGMENTED_IMAGES, file[:-4]+f"_{counter}.jpg")
    return file_path