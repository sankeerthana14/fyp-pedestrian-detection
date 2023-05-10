# Blackout - An Augmentation Technique for Occlusion Handling in Pedestrian Detection

## Abstract
Pedestrian Detection has numerous applications, ranging from autonomous driving to traffic analysis. One inherent challenge faced in the field of pedestrian detection is the problem of occluded objects. In this project, we propose Blackout - a novel enhancement to an existing data augmentation Cutout, which tackles intraclass occlusion, where a pedestrian is blocked by another pedestrian.

Blackout is a strong augmentation technique that blacks out the intersection of overlapping ground truth bounding boxes. It does so by computing the intersection over union of the ground truth bounding boxes present in an image and blacks out the intersection of the ground truth bounding boxes if the intersection over union values lies within the threshold range. Blackout has been evaluated on the Penn Fudan Pedestrian Detection Dataset.

Through our evaluation of Blackout, it can be concluded that Blackout implemented as a standalone strong augmentation technique on larger models can result in a large increase in accuracy – a 13% increase in accuracy in the case of the state-of-the-art model You Only Live Once eXtreme – Medium sized model (YOLOX-M). Blackout can also be used as an additional augmentation along with other existing augmentations as it results in a 1% and 2% increase in accuracy in YOLOX-S and YOLOX-M respectively.

Therefore, Blackout can prove to be extremely useful in cases where we would want to force the model to learn from the outlines of the objects. This can include a myriad of applications in field such as crowd tracking and control.
