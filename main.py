import cv2
from mpi4py import MPI
import time
import teste_filterlinear


tini = time.time()

comm = MPI.COMM_WORLD

imgsrc = "C:\\Users\\Kodo\\PycharmProjects\\ProcImg\\john_lennon_capa_widelg.jpeg"

teste_filterlinear.main(imgsrc)

#img = cv2.imread(imgsrc, 0)
#
#print("%d of %d" % (comm.Get_rank(), comm.Get_size()))
#if(comm.Get_rank() == 0):
#    res = cv2.bitwise_not(img)
#    tfim = time.time() - tini
#    print("Tempo de Processamento: ", tfim)
#    cv2.imshow('image', res)
#    cv2.waitKey(0)
#   cv2.destroyAllWindows()
#if(comm.Get_rank() == 1):
#    res = cv2.resize(img, (600, 650))
#    tfim = time.time() - tini
#    print("Tempo de Processamento: ", tfim)
#    cv2.imshow('image', res)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()


