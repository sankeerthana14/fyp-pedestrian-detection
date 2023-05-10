#DUPLICATING THE XML FILES OF THE AUGMENTED IMAGES

import xml.etree.ElementTree as ET
import HELPER as HELPER
import shutil
import os

aug_contents = HELPER.remove_DS_Store(os.listdir(HELPER.AUGMENTED_IMAGES))
xml_contents = HELPER.remove_DS_Store(os.listdir(HELPER.ANNOTATIONS))

#duplicating the existing annotations
def duplicate_xml():
    for file in aug_contents:
        filename = file.split('_')
        source = os.path.join(HELPER.ANNOTATIONS, filename[0]+'.xml')
        destination = os.path.join(HELPER.AUGMENTED_ANNOTATIONS, str(file[:-4]+'.xml'))
        shutil.copyfile(source, destination)

#need to change the path in <path> to contain the _0.jpg instead of only the name and the folder
# name in tag <folder> and the filename as well in <filename>
def modify_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    for tag in root.findall('path'):
        elements = file.split('/')
        new_img = elements[-1][:-4]
        #org thought of this but the vocdevkit version is diff
        #new_path = os.path.join(HELPER.AUGMENTED_IMAGES, str(new_img + '.jpg'))

        tag.text = str(new_img + '.jpg')

    for element in root.findall('filename'):
        element.text = new_img + '.jpg'

    for folder_name in root.findall('folder'):
        #different than the vocdevkit version - hence changing it to that
        #folder_name.text = 'augmented_images'

        folder_name.text = ''

    tree.write(file)

#reading all the .xml files in the augmented_annotations folder and calling the modify_xml() on it
aug_xml_contents = HELPER.remove_DS_Store(os.listdir(HELPER.AUGMENTED_ANNOTATIONS))

for element in aug_xml_contents:
    file = os.path.join(HELPER.AUGMENTED_ANNOTATIONS, element)
    modify_xml(file)

for element in xml_contents:
    file = os.path.join(HELPER.ANNOTATIONS, element)
    modify_xml(file)






