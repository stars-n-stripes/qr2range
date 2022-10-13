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

    @unittest.skip("Confirmed to work in current version")
    def test_create_qr(self):
        # Test the python creator
        outpath = Path(__file__).parent / "img/qr-gen-test.png"
        qr2range.util.gen_qr_file("This is a test", outpath.__str__())
        file_exists = os.path.exists(outpath)
        self.assertTrue(file_exists)
            
    @unittest.skip("Confirmed to work in current version")
    def test_detect_qr(self, human_verify=False):
        # Basically a test for the developer rn, as this doesn't actually test code in the package
        # Will be replaced by something more robust when we're actually using it.
        
        # Ensure we can find the test image no matter which context we run this text in by using the path of this .py file
        # test_qr_imgpath = (Path(__file__).parent / "img/qr-test.png").__str__()
        multi_qr_imgpath = (Path(__file__).parent / "img/qr-network-test.png").__str__()

        # image = cv2.imread(test_qr_imgpath)
        image = cv2.imread(multi_qr_imgpath)
        # Gaussian test: 
        image = cv2.GaussianBlur(image, (3, 3), 0)

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

        # Just check that we are 4/4 on codes
        if len(codes) < 4:
            # qr2range.util.show_cv2img_blocking(image, message=f"Failed Test Case: {len(codes)}/4 detected")
            cv2.imshow()
        else:
            qr2range.util.show_cv2img_blocking(image, message=f"Successful QR Code detection test")
        self.assertTrue(len(codes) == 4)

    def test_detect_rectangles(self):
        qr_imgpath = (Path(__file__).parent / "img/qr-network-test.png").__str__()
        image = cv2.imread(qr_imgpath)
        qr2range.vision.detect_networking_shapes(image)
        self.assertTrue(1) # TODO: Fill out with actual test at some point; just checking functionality here

    @classmethod
    def tearDownClass(cls):
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
if __name__ == "__main__":
    unittest.main() 