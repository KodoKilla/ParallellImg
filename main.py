"""
Filtrando imagens de forma paralela com MPI no Python
Os filtros utilizados são todos da biblioteca OpenCV, importada como cv2
As imagens foram retiradas do google
"""

import cv2
from mpi4py import MPI
import time
import FilterLinear

comm = MPI.COMM_WORLD

imgsrc = "C:\\Users\\Kodo\\PycharmProjects\\ProcImg\\john_lennon_capa_widelg.jpeg"
if(comm.Get_rank() != 0 and comm.Get_rank() != 0):
    imgsrc = "C:\\Users\\Kodo\\PycharmProjects\\ProcImg\\ruido.jpg"

print("Processo %d de %d" % (comm.Get_rank(), comm.Get_size()))

res, nomeFiltro = FilterLinear.main(imgsrc, comm.Get_rank())

cv2.imshow(nomeFiltro, res)
c = cv2.waitKey(0)

#Comando para executar no console: mpiexec -n 4 python main.py
