from re import A
from mpi4py import MPI

COMM=MPI.COMM_WORLD
RANK=COMM.Get_rank()
SIZE=COMM.Get_size()
tag=99

if RANK==0:
    data=int(input("From process {RANK}, enter the number of process : ".format(RANK=RANK)))
    for i in range(1,4):
        COMM.send(data,dest=i,tag=tag)
          
else:
    rec=COMM.recv(source=0,tag=tag)
    print("Process {RANK}, value = {v}".format(RANK=RANK,v=rec))
COMM.barrier()    