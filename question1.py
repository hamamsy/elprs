import cv2
import numpy as np
from matplotlib import pyplot as plt
from utils import getColorClasses,applyLabelColors,generateRandomColors,showImage
from cciter import connectedComponentsIter
from ccdfs import connectedComponentsDfs

def ConnectedComponents(algo='Iter',image=None):
    max_rows      = image.shape[0]
    max_cols      = image.shape[1]
    max_label     = max_rows * max_cols
    color_class   = getColorClasses(image)
    if(algo == 'Iter'):
        labels    = connectedComponentsIter(color_class, max_label)
    else:
        labels    = connectedComponentsDfs(color_class, max_label)
    colors        = generateRandomColors(max_label)
    result        = applyLabelColors(labels, colors, max_rows, max_cols)
    return result

img = cv2.imread('images/L1.jpg',0)
ret,binary_image = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #CONVERTING L1.jpg TO BINARY

img2 = cv2.imread('images/L3.jpg',0)
#labels_dfs = connectedComponentsDfs(getColorClasses(binary_image), 2000)

# for himography transformation
max_rows      = img2.shape[0]
max_cols      = img2.shape[1]
src_pts       = np.float32([[5, 3],[998, 131],[925, 691],[66, 476]])
dst_pts       = np.float32([[0, 0],[max_cols-1, 0],[max_cols-1, max_rows-1],[0, max_rows-1]])
h_matrix,ret  = cv2.findHomography(src_pts,dst_pts)
fv_image      = cv2.warpPerspective(src=img2, M=h_matrix, dsize=(max_cols, max_rows))


print("Enter '1' to answer the first part, or '2' to answer the second part\n Enter 0 to exit")
t = eval(input())
if(t==1):
    image   = binary_image
else:
    image   = fv_image

print("Enter '1' for the Iterative algorithim, or '2' for the Dfs algorithim")
t = eval(input())
if(t==1):
    result_image = ConnectedComponents('Iter',image)
else:
    result_image = ConnectedComponents('Dfs',image)
showImage("Connected Components on Binary Image",result_image)
