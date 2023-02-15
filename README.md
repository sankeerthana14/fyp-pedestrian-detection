# Final Year Project - Pedestrian Detection
__Repo Name: fyp-pedestrian-detection__
__Dataset Used: Penn Fudan Dataset__

The aim of this project is to improve the performance of the YOLOX Model by improving the accuracy of the YOLOX model in the use case of Pedestrian Detection. One of the approaches adopted was to come up with new data augmentation techniques to improve the model's learning and performance on occluded pedestrians.

There are two types of occlusion - Inter-class Occlusion and Intra-class Occlusion. This approach deals mostly with the Intra-class Occlusion where one pedestruan occludes another pedestrian. The idea behind this approach is to calculate the Intersection Over Union (IoU) of the ground truth classes and for the images where the boxes that have an IoU between 0.20 and 0.50, their intersection is blacked out. This allows the model to learn only from the parts of the pedestrian that are visible - ie: learns from only part of the object. 

### Preprocessing



