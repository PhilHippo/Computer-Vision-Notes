import cv2
import numpy as np
import matplotlib.pyplot as plt

def onClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(dst_points) < 4:
            dst_points.append([x,y])
            cv2.circle(img_copy,(x,y),50,(0,0,255),-1)
            cv2.imshow('base img', img_copy)

#load the two images
base_img = cv2.imread(r'Homework 1\img\billboard.jpg')
img_copy = base_img.copy()
img2 = cv2.imread(r'Homework 1\img\axolotl.jpg')
#get images data
base_h, base_w = base_img.shape[:2]
img2_h, img2_w = img2.shape[:2]

#create source and destination points sets
src_points = np.array([[0,0],[0,img2_h],[img2_w,img2_h],[img2_w,0]], dtype=np.float32)
dst_points = []

cv2.namedWindow('base img', cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback('base img', onClick)
#cv2.namedWindow('img 2', cv2.WINDOW_KEEPRATIO)

cv2.imshow('base img', base_img)
#cv2.imshow('img 2', img2)
cv2.waitKey(0)

#computing the homography matrix
dst_float = np.array(dst_points,dtype=np.float32)
H = cv2.getPerspectiveTransform(src_points,dst_float)

#apply H to the image to be warped
warped = cv2.warpPerspective(img2,H,(base_w,base_h))
#create the mask
mask = np.zeros(base_img.shape,dtype=np.uint8)

#set to white the pixels that we want to copy in the billboard
cv2.fillConvexPoly(mask,np.int32(dst_points),(255,255,255))

#invert the mask
mask = cv2.bitwise_not(mask)

#apply the mask to the billboard image
mask_bill = cv2.bitwise_and(base_img, mask)

#apply mask to the warped image
final_img = cv2.bitwise_or(mask_bill, warped)
cv2.destroyAllWindows()

#show the final image
cv2.namedWindow('final_image', cv2.WND_PROP_ASPECT_RATIO)
cv2.imshow('final_image', final_img)
cv2.waitKey(0)
