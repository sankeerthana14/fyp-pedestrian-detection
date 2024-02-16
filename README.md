# Blackout - An Augmentation Technique for Occlusion Handling in Pedestrian Detection

## Abstract
Pedestrian Detection has numerous applications, ranging from autonomous driving to traffic analysis. One inherent challenge faced in the field of pedestrian detection is the problem of occluded objects. This project proposes Blackout - a novel enhancement to an existing data augmentation Cutout, which tackles intraclass occlusion, where a pedestrian is blocked by another pedestrian.

Blackout is a strong augmentation technique that blacks out the intersection of overlapping ground truth bounding boxes. It does so by computing the intersection over union of the ground truth bounding boxes present in an image and blacks out the intersection of the ground truth bounding boxes if the intersection over union values lies within the threshold range. Blackout has been evaluated on the Penn Fudan Pedestrian Detection Dataset.

Through our evaluation of Blackout, it can be concluded that Blackout implemented as a standalone strong augmentation technique on larger models can result in a large increase in accuracy – a 13% increase in accuracy in the case of the state-of-the-art model You Only Live Once eXtreme – Medium sized model (YOLOX-M). Blackout can also be used as an additional augmentation along with other existing augmentations as it results in a 1% and 2% increase in accuracy in YOLOX-S and YOLOX-M respectively.

Therefore, Blackout can prove to be extremely useful in cases where we would want to force the model to learn from the outlines of the objects. This can include a myriad of applications in field such as crowd tracking and control.

## Usage
### Processing Files
1. **blackout.py** - contains the function to blackout the intersection of the overlapping bounding boxes.
2. **display_box_xml.py** - contains the code to read from the xml annotations of the images and displaying the bounding boxes and logic to calculate the IoU.
3. **augmentation.py** - contains the code to compile the functions in the above 2 python files, caluclate the IoU values and implement the blackout algorithm and store the augmented images.
4. **duplicating_xml.py** - contains the code to duplicate the corresponding annotations of the augmented images.
5. **split_train_test.py** - contains the code to split the dataset into train, test and validation split.
6. **helper.py** - contains the paths to the respective folders and some helper functions.

### Model Training Files
1. **YOLOX_Training.ipynb** - contains the code to train the different versions of YOLOX (YOLOX-S and YOLOX-M).
2. **State-of-the-art Comparison.ipynb** - contains the code to train the corresponding state of the art models (CentreNet, EfficientDet) in order to compare with the YOLOX model.
3. **SOTA_YOLOv6.ipynb** - contains the code for inferencing the YOLOv6 model on the dataset, this notebook can be used as a continuation to train the YOLOv6 as well.

## Extension of FYP
As a part of the extension, the plan is to conduct state-of-the-art comparison to compare the YOLOX model's performance with the proposed BlackOut algorithm implemented on the **YOLOv6 model, CentreNet and EfficientDet**. 

Note that the 3 different models have reported their results on different datasets, for example YOLOv6 - COCO dataset etc. SOTA models can be picked from this link: https://paperswithcode.com/task/real-time-object-detection
