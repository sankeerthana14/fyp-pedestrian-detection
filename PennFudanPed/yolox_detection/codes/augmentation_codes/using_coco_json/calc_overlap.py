#CALCULATIING THE PERCENTAGE OF OVERLAP
from display_bbox import annots_info as ANNOT_INFO

def iou(list1, list2):
    """
    where list1 and list2 are the predictions as annot_info values for box1 and box2
    given the top left coordinates (x,y)
    »» BBox1:
    • Lower Left Corner - (x1,y1)
    • Upper Right Corner - (a1, b1)

    »» BBox2:
    • Top Left Corner - (x2, y2)
    • Bottom Right Corner - (a2, b2)
    """
    #Initialising BBox1 values
    x1 = list1[0]
    y1 = list1[3] - list1[1]
    a1 = list1[0] + list1[2]
    b1 = list1[1]

    #Initisalising BBox2 values
    x2 = list2[0]
    y2 = list2[3] - list2[1]
    a2 = list2[0] + list2[2]
    b2 = list2[1]

    """
    Let Intersection area coordinate details be:
    • Bottom Left - (xx, yy)
    • Top Right - (aa, bb)
    """

    #Intersection coordinates
    xx = max(x1, x2)
    yy = max(y1, y2)
    aa = min(a1, a2)
    bb = min(b1, b2)

    #Intersection width, height and area
    w = max(0, aa-xx)
    h = max(0, bb-yy)

    intersection_area = w * h

    #Union area of both the boxes
    bbox1_area = list1[2] * list2[3]
    bbox2_area = list2[2] * list2[3]

    union_area = bbox1_area + bbox2_area - intersection_area

    #Calculating IoU 
    IoU = intersection_area / union_area

    return IoU
print(ANNOT_INFO)
print(iou([63, 89, 129, 296], [125, 97, 106, 276]))




