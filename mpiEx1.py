from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(rank)

if rank == 0:
	data = [1,2,3]
	comm.send(data, dest=1)
elif rank == 1:
	data = comm.recv(source=0)