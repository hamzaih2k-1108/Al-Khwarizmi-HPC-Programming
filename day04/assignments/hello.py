from mpi4py import MPI

COMM=MPI.COMM_WORLD
RANK=COMM.Get_rank()
SIZE=COMM.Get_size()
print("Hello from the rank {RANK} process".format(RANK=RANK))
COMM.barrier() # the communicator can pass the barrier until all processus call the function
if RANK==3:
  print("Parallel execution of hello_world with {SIZE} process".format(SIZE=SIZE))