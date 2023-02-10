#CONSOLIDATED PATHS FOR THE CODE
import os

PARENT = "/Users/sankeerthana/Documents/NTU/YEAR_4/FYP/fyp-pedestrian-detection/PennFudanPed/yolox_detection"

#MAIN OUTER FOLDERS
#contains .xml files
ANNOTATIONS = os.path.join(PARENT, 'annotations') 

#contains all the codes relevant
CODES = os.path.join(PARENT, 'codes') 

#contains the .jpg images
IMAGES = os.path.join(PARENT, 'images') 

#contains the augmented .jpg images
AUGMENTED_IMAGES = os.path.join(PARENT, 'augmented_images')

#SUB FOLDERS
AUGMENTATION_CODES = os.path.join(CODES, 'augmentation_codes')
USING_XML = os.path.join(AUGMENTATION_CODES, 'using_xml')


#HELPER FUNCTIONS
def remove_DS_Store(list1):
    if '.DS_Store' in list1:
        list1.remove('.DS_Store')
    return list1

def remove_ipynb_checkpoints(list1):
    if '.ipynb_checkpoints' in list1:
        list1.remove('.ipynb_checkpoints')
    return list1