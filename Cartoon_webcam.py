import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
while True:
    img= cap.read()[1]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #apply median blur to remove noise
    img_gray = cv2.medianBlur(img_gray, 5)

    # extract the edges with laplacian filter
    edges = cv2.Laplacian(img_gray, cv2.CV_8U,ksize=5)

    #every pixel above 70 will be set to white, below 70 to black
    _, thresholded = cv2.threshold(edges, 70,255,cv2.THRESH_BINARY_INV)

    # GET the color with bilateral filter
    color_img = cv2.bilateralFilter(img,10,250,250) 

    # merge the colors and edges
    skt = cv2.cvtColor(thresholded,cv2.COLOR_GRAY2BGR)

    sketch_img = cv2.bitwise_and(color_img,skt)

    cv2.imshow("cartoon",cv2.flip(sketch_img,1))
    k = cv2.waitKey(4)
    if k == ord('q'):
        break