#SPLITTING IMAGES INTO TRAIN-TEST-VALIDATION

#Total # of Images = 170

import random
import os

PATH = os.path.join(os.getcwd(),'yolox_detection', 'images')

contents = os.listdir(PATH)

TOTAL = len(contents)

NUM_TRAIN = int(TOTAL * 0.8)
NUM_TEST = int(TOTAL * 0.1)
NUM_VALID = int(TOTAL * 0.1)

print(f"Train: {NUM_TRAIN}")
print(f"Test: {NUM_TEST}")
print(f"Valid: {NUM_VALID}")

train = random.choices(contents)

os.chdir('yolox_detection/images')

tags = {'train': NUM_TRAIN, 'test': NUM_TEST, 'valid': NUM_VALID}

def split_data(tag):
    for i in range(3):
        os.mkdir(tag)
        contents = l
        temp = random.choices()

        #temp = random.choice(contents, )

