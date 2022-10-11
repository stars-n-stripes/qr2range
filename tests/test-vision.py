import cv2
import sys
from pathlib import Path

# =============================
# Add qr2range package to path for tests
project_abspath = Path(__file__).parent.parent.absolute()
print(project_abspath)
sys.path.append(project_abspath.__str__())
# =============================

import qr2range.vision, qr2range.util
import os
import unittest

class TestVision(unittest.TestCase):
    def test_create_qr(self):
        # Test the python creator
        outpath = Path(__file__).parent / "img/qr-gen-test.png"
        qr2range.util.gen_qr_file("This is a test", outpath.__str__())
        file_exists = os.path.exists(outpath)
        self.assertTrue(file_exists)
            

    def test_detect_qr(self, human_verify=False):
        # Basically a test for the developer rn, as this doesn't actually test code in the package
        # Will be replaced by something more robust when we're actually using it.
        
        # Ensure we can find the test image no matter which context we run this text in by using the path of this .py file
        # test_qr_imgpath = (Path(__file__).parent / "img/qr-test.png").__str__()
        multi_qr_imgpath = (Path(__file__).parent / "img/qr-network-test.png").__str__()

        # image = cv2.imread(test_qr_imgpath)
        image = cv2.imread(multi_qr_imgpath)
        detector = cv2.QRCodeDetector()

        retval, decodedTexts, codes, _ = detector.detectAndDecodeMulti(image)

        # decodedText, points, _ = detector.detectAndDecode(image)
        if retval and codes is not None:
            for i in range(codes.shape[0]):
                qr_point_group = codes[i,:]
                for j in range(len(qr_point_group)):
                    next_idx = (j+1) % len(qr_point_group)
                    cv2.line(image, tuple(qr_point_group[j].astype(int)), tuple(qr_point_group[next_idx].astype(int)), (255, 0, 0), 5)
                # print(f"Detected Code: {decodedTexts[i]}")
        
        if human_verify:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.assertTrue(input("Press ENTER to confirm the image looked good; enter 'N' to reject: ") == "")
        
        else:
            # Just check that we are 4/4 on codes
            self.assertTrue(len(codes) == 4)

    def test_detect_rectangles(self):
        qr_imgpath = (Path(__file__).parent / "img/qr-network-test.png").__str__()
        image = cv2.imread(qr_imgpath)
        qr2range.vision.detect_whiteboard_rectangles(image)
        self.assertTrue(1) # TODO: Fill out with actual test at some point; just checking functionality here

        
if __name__ == "__main__":
    unittest.main() 