import cv2
import os
import numpy as np

train_list = open('list/train.txt').readlines()
test_list = open('list/test.txt').readlines()
'''
for i in train_list:
	cmd = 'cp images/'+i[:-1]+' train/images/'
	os.system(cmd)
	cmd = 'cp labels/'+i[:-1]+' train/masks/'
	os.system(cmd)
for i in test_list:
	cmd = 'cp images/'+i[:-1]+' test/images/'
	os.system(cmd)
	cmd = 'cp labels/'+i[:-1]+' test/masks/'
	os.system(cmd)
'''
for i in train_list:
	img = cv2.imread('images/'+i[:-1])
	img = cv2.resize(img, (448, 448))
	cv2.imwrite('train/images/'+i[:-1],img)
	msk = cv2.imread('labels/'+i[:-1])
	msk = cv2.resize(msk, (448, 448))
	msk = np.minimum(msk[:,:,0], np.ones((448,448)))
	cv2.imwrite('train/masks/'+i[:-1],msk)
for i in test_list:
	img = cv2.imread('images/'+i[:-1])
	img = cv2.resize(img, (448, 448))
	cv2.imwrite('test/images/'+i[:-1],img)
	msk = cv2.imread('labels/'+i[:-1])
	msk = cv2.resize(msk, (448, 448))
	msk = np.minimum(msk[:,:,0], np.ones((448,448)))
	cv2.imwrite('test/masks/'+i[:-1],msk)
