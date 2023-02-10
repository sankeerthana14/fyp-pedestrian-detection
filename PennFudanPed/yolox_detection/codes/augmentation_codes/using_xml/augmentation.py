#COMBINING EVERYTHING INTO SINGLE FLOW - generating the augmented images

import display_box_xml as DISPLAY_BOX
import black_out as BLACK_OUT
import HELPER as HELPER
import os

#READING THE XML FILES
#Getting the xml filenames
contents = os.listdir(HELPER.ANNOTATIONS)
contents = HELPER.remove_DS_Store(contents)
contents = HELPER.remove_ipynb_checkpoints(contents)

#dictionary that contains a dictionary fo predictions according to image names
img_preds = {}

#for each file create an annot_info with the details of all the bounding boxes
for files in contents:
    file_path = os.path.join(HELPER.ANNOTATIONS, files)
    annot_info = DISPLAY_BOX.read_xml(file_path)
    img_preds[files] = annot_info
   
    #need to put all the lists in one list
    info = list(annot_info.values())

    #display boxes
    IMG_PATH = os.path.join(HELPER.IMAGES, str(files[:-4]+'.jpg'))
    DISPLAY_BOX.display_box(IMG_PATH, info)


#calculating IoU
iou_dict = {}

for image, preds in img_preds.items():
    iou_dict[image] = []
    if len(preds) == 1:
        pass
    else:
        #calculating the iou for each box with every other element
        for i in range(len(preds)):
            for j in range(i, len(preds)):
                if i == j:
                    continue
                else:
                    x_left, y_top, x_right, y_bottom, IoU = DISPLAY_BOX.calc_iou(preds[i], preds[j])
                    res = [x_left, y_top, x_right, y_bottom, IoU]
                    if IoU != 0:
                        iou_dict[image].append(res)

#removing the key value pairs when the value is an empty list []
for key in list(iou_dict.keys()):
    if iou_dict[key] == []:
        del iou_dict[key]

#creating and storing the augmented images
for image, iou in iou_dict.items():
    counter = 0
    for preds in iou:
        if 0.20 < preds[-1] < 0.50:
            image_path = os.path.join(HELPER.IMAGES, str(image[:-4]+'.jpg'))
            BLACK_OUT.black_out(image_path, preds[0], preds[1], preds[2], preds[3], counter)
            counter += 1

#duplicating the .xml files to have the same name as the augmented_images