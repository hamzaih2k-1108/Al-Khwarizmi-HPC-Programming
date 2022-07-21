from mpi4py import MPI

COMM=MPI.COMM_WORLD
RANK=COMM.Get_rank()


if RANK==0:
    data=int(input("From process {RANK}, enter an integer : ".format(RANK=RANK)))
    
else:
    data=None
    
data=COMM.bcast(data,root=0)    
print("process {RANK} got {data}".format(RANK=RANK,data=data))    
  

