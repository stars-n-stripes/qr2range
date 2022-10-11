import cv2
import pyqrcode

def gen_qr_file(data, outfile=None, scale=5):
    qr = pyqrcode.create(data)
    qr.png(outfile, scale=scale)
    
def show_cv2img_blocking(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
