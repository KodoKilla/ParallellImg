import cv2
from mpi4py import MPI
import time
import SEQ_FilterLinear


tini = time.time()

imgsrc = "C:\\Users\\Kodo\\PycharmProjects\\ProcImg\\john_lennon_capa_widelg.jpeg"

SEQ_FilterLinear.main(imgsrc)



