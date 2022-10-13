import cv2
from . import util
import numpy as np

def detect_networking_shapes(img, hsv_filter_low=None, hsv_filter_high=None):

    # ======= Pre-Processing ======
    # Smooth the image
    gaussian_img = cv2.GaussianBlur(img, (3, 3), 0)

    # ======= Red Filter ======= 
    # default params
    if not hsv_filter_low:
        hsv_filter_low = np.array([0, 50, 50])
    if not hsv_filter_high:
        hsv_filter_high = np.array([0, 255, 255])
    
    hsv_img = cv2.cvtColor(gaussian_img, cv2.COLOR_BGR2HSV)
    # Process the image
    mask = cv2.inRange(hsv_img, hsv_filter_low, hsv_filter_high)
    result = cv2.bitwise_and(img, img, mask=mask)

    # Two-mask process for reference, if we need it when testing real images
    # ref: https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv
    # # lower mask (0-10)
    # lower_red = np.array([0,50,50])
    # upper_red = np.array([10,255,255])
    # mask0 = cv2.inRange(hsv_img, lower_red, upper_red)

    # # upper mask (170-180)
    # lower_red = np.array([170,50,50])
    # upper_red = np.array([180,255,255])
    # mask1 = cv2.inRange(hsv_img, lower_red, upper_red)

    # # join my masks
    # mask = mask0+mask1

    # set my output img to zero everywhere except my mask
    # output_img = img.copy()
    # output_img[np.where(mask==0)] = 0

    # ======= Red Filter ======= 

    # Now, we can select corners
    # TODO: This seems like a good list of OpenCV subtasks to get what we need:
    # https://stackoverflow.com/a/7263794

    # 1. Convert from RGB to grayscale
    grayscale_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # 2. Blur (done above)

    # 3. Detect corners (+ edges)
    corner = cv2.cornerHarris(grayscale_result, 2, 3, 0.04)
    edges = cv2.Canny(grayscale_result, 50, 150)

    # Detect contours from Canny and findContours
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    thresh, binary_result = cv2.threshold(grayscale_result, 50, 255, cv2.THRESH_BINARY)

    # contour_img = img.copy()
    # cv2.drawContours(image=contour_img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    # Generate a test image showing the corners
    corner_mask = np.zeros_like(grayscale_result)
    corner_mask[corner>0.01*corner.max()] = 255 # simple thresholding to make the corners white

    # Generate a test image showing the edges    
    # cv2.imshow("Corner Detections", corner_mask)
    # cv2.imshow("Edge Detections", edges)
    # cv2.imshow("Contours", contour_img)

    # Show binary img
    cv2.imshow("Binary result", binary_result)


