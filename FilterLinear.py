import cv2
from mpi4py import MPI
import time

def main(imgsrc, nProcesso):
    tini = time.time()
    img = cv2.imread(imgsrc, 0)

    if (nProcesso == 0):
        tipo = "Reverso"
        res = cv2.bitwise_not(img)
        tfim = time.time() - tini
        print("Tempo de Processamento: ", tfim)
    if (nProcesso == 1):
        tipo = "Resize"
        res = cv2.resize(img, (600, 650))
        tfim = time.time() - tini
        print("Tempo de Processamento: ", tfim)
    if (nProcesso == 2):
        tipo = "Gaussiano"
        res = cv2.GaussianBlur(img, (5, 5), 0)
        tfim = time.time() - tini
        print("Tempo de Processamento: ", tfim)
    if (nProcesso == 3):
        tipo = "Média"
        res = cv2.medianBlur(img, 5)
        tfim = time.time() - tini
        print("Tempo de Processamento: ", tfim)

    return res, tipo