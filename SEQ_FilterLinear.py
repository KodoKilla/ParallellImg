"""
Baseado no exemplo do website oficial do OpenCV

"""
import sys
import cv2 as cv
import numpy as np
import time


def main(argv):
    tini = time.time()
    window_name = 'Filtro Linear'

    imageName = argv
    # Loads an image
    src = cv.imread(imageName, cv.IMREAD_COLOR)
    # Check if image is loaded fine

    ddepth = -1

    ind = 0
    while ind != 4:

        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)

        dst = cv.filter2D(src, ddepth, kernel)

        cv.imshow(window_name, dst)

        ind += 1
    tfim = time.time() - tini
    print("Tempo de Processamento: ", tfim)
    return 0

