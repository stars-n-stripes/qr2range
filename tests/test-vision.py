from base64 import decode
import cv2
from pathlib import Path

# Ensure we can find the test image no matter which context we run this text in by using the path of this .py file
# test_qr_imgpath = (Path(__file__).parent / "img/qr-test.png").__str__()
multi_qr_imgpath = (Path(__file__).parent / "img/qr-network-test.png").__str__()

# image = cv2.imread(test_qr_imgpath)
image = cv2.imread(multi_qr_imgpath)
detector = cv2.QRCodeDetector()

retval, decodedTexts, points, _ = detector.detectAndDecodeMulti(image)
print(retval)

# decodedText, points, _ = detector.detectAndDecode(image)
if points is not None:
    for i in range(points.shape[0]):
        qr_point_group = points[i,:]
        print(qr_point_group)
        for j in range(len(qr_point_group)):
            print(qr_point_group[j].shape)
            next_idx = (j+1) % len(qr_point_group)
            print(tuple(qr_point_group[j]))
            print(tuple(qr_point_group[next_idx]))
            cv2.line(image, tuple(qr_point_group[j].astype(int)), tuple(qr_point_group[next_idx].astype(int)), (255, 0, 0), 5)
            # cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
        print(decodedTexts[i])

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()