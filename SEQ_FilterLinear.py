"""
@file filter2D.py
@brief Sample code that shows how to implement your own linear filters by using filter2D function
"""
import sys
import cv2 as cv
import numpy as np


def main(argv):
    window_name = 'Filtro Linear'

    imageName = argv
    # Loads an image
    src = cv.imread(imageName, cv.IMREAD_COLOR)
    # Check if image is loaded fine

    ddepth = -1

    ind = 0
    while True:

        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)

        dst = cv.filter2D(src, ddepth, kernel)

        cv.imshow(window_name, dst)
        c = cv.waitKey(0)
        if c == 27:
            break
        ind += 1
    return 0

