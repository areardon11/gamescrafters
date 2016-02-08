from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(rank)

if rank == 0:
    data = [1,2,3,4,5]
else:
    data = []

#Scatter
data = comm.scatter(data, root=0)
print "rank", rank, "recieved", data
data = data + 2

#Gather
data = comm.gather(data, root=0)

comm.Barrier()

if rank == 0:
    print data