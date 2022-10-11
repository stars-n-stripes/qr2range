import cv2
from . import util
import numpy as np

def detect_whiteboard_rectangles(img, hsv_filter_low=None, hsv_filter_high=None):

    # ======= Red Filter ======= 
    # default params
    if not hsv_filter_low:
        hsv_filter_low = np.array([0, 50, 50])
    if not hsv_filter_high:
        hsv_filter_high = np.array([0, 255, 255])
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
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
    
    
    
    util.show_cv2img_blocking(result)

