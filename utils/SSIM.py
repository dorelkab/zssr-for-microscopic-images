from skimage.measure import compare_ssim
from scipy.stats import pearsonr
import scipy
import argparse
import imutils
import cv2

import numpy as np

imageB = cv2.imread("compare\\converted.png")
imageA = cv2.imread("compare\\ZSSR_0.png")
d=(imageB.shape[1],imageB.shape[0])
imageA = cv2.resize(imageA,d)

# #SSIM
# (score, diff) = compare_ssim(imageA, imageB, full=True, multichannel=True)
# diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))

#NORMAL PCC
# n1=np.array(imageA)
# n2=np.array(imageB)
# pear = scipy.stats.pearsonr(np.array(imageA[:,:,0]).flatten(), np.array(imageB[:,:,0]).flatten())
# print(pear[0])

# P METRIC
# x1 = 0
# y1 = 0
# M = imageB.shape[0]//32
# N = imageB.shape[1]//32
# indx_store = []
# pears = np.empty(shape=(32*32,2))
# i=0
# for y in range(0,imageB.shape[0],M):
#     for x in range(0, imageB.shape[1], N):
#         y1 = y + M
#         x1 = x + N
#         tilesB = imageB[y:y + M, x:x + N]
#         tilesA = imageA[y:y + M, x:x + N]
#         # grayB = cv2.cvtColor(tilesB, cv2.COLOR_BGR2GRAY)
#         # grayA = cv2.cvtColor(tilesA, cv2.COLOR_BGR2GRAY)
#         pears[i] = scipy.stats.pearsonr(np.array(tilesA[:, :, 0]).flatten(), np.array(tilesB[:, :, 0]).flatten())
#         # pears[i] = scipy.stats.pearsonr(np.array(grayA[:, :]).flatten(), np.array(grayB[:, :]).flatten())
#         if ((tilesB[:, :, 0] > 140).any()):
#         # if ((tilesB[:, :, 0] > 90).any()):
#         #     cv2.imshow('image',tilesB)
#         #     cv2.waitKey()
#         #     cv2.imshow('image', tilesA)
#         #     cv2.waitKey()
#             indx_store.append(i)
#         i += 1
# pear_reduced_mean = np.mean(pears[indx_store])
# print(pear_reduced_mean)

#segmentation PCC
vect_A = []
vect_B = []
for y in range(imageB.shape[0]):
    for x in range(imageB.shape[1]):
        if ((imageB[y, x, 0] > 100).any()):
            vect_A.append(imageA[y, x, 0])
            vect_B.append(imageB[y, x, 0])
pear = scipy.stats.pearsonr(np.array(vect_A), np.array(vect_B))
print(pear[0])