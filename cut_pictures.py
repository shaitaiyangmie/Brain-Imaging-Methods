import cv2.cv2 as cv2
import os
import numpy as np


# print('root:', root)
# list_name = os.listdir(root)
# list_name = [name for name in list_name if name[0] != '.']
# print(list_name)
# for name in list_name:
root = ''
img_dir = root
img = cv2.imread(img_dir)
bbox = cv2.selectROI(img, False)
cut = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
cv2.imwrite('/Users/shaotianyu01/Desktop/school/11.4/cut_new/', cut)
# cv2.imwrite('/Users/shaotianyu01/Desktop/school/img_pred/cut_{}.jpg'.format(name), cut)
