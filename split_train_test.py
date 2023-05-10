#SPLITTING THE DATA INTO TRAIN-TEST-VALIDATION + STORING IN A TEXT FILE

import HELPER as HELPER
import random
import os

contents = HELPER.remove_DS_Store(HELPER.remove_ipynb_checkpoints(os.listdir(HELPER.IMAGES)))

TOTAL = len(contents)

NUM_TRAIN = int(TOTAL * 0.8)
NUM_TEST = int(TOTAL * 0.1)
NUM_VALID = int(TOTAL * 0.1)

print(f"Total: {TOTAL}")
print(f"Train: {NUM_TRAIN}")
print(f"Test: {NUM_TEST}")
print(f"Valid: {NUM_VALID}")

train = random.sample(contents, k=NUM_TRAIN)

contents_set = set(contents)
train_set = set(train)

#remaining files - after removing the training ones
remaining_contents = list(contents_set - train_set)

valid = random.sample(remaining_contents, k=NUM_VALID)
valid_set = set(valid)
    
#getting the test set
test = list(set(remaining_contents) - valid_set)

train = [x+"\n" for x in train]
valid = [y+"\n" for y in valid]
test = [z+"\n" for z in test]

#writing into text file
with open('yolox_detection/train.txt', 'w') as f:
    f.writelines(train)

with open('yolox_detection/valid.txt', 'w') as f:
    f.writelines(valid)

with open('yolox_detection/test.txt', 'w') as f:
    f.writelines(test)


    









