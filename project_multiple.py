import cv2
import numpy as np
from utils import get_four_points

if __name__ == '__main__':
    
    cap = cv2.VideoCapture(0)
    s, im = cap.read() # captures image
    cv2.imshow("Test Picture", im) # displays captured image
    cv2.imwrite("test.bmp",im) # writes image test.bmp to disk
    
    im_src = cv2.imread("test.bmp")
    size = im_src.shape

    pts_src = np.array(
        [
            [0,0], [size[1] - 1, 0], [size[1] - 1, size[0] - 1], [0, size[0]- 1]
            ], dtype = float
        )

    im_dst = cv2.imread("times-square.jpg")
    
    while (True):
        pts_dst = get_four_points(im_dst)

        h,status = cv2.findHomography(pts_src, pts_dst);

        im_temp = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

        cv2.fillConvexPoly(im_dst, pts_dst.astype(int), 0, 16);

        im_dst = im_dst + im_temp;

        cv2.imshow("Image", im_dst);
    cv2.waitKey(0);
