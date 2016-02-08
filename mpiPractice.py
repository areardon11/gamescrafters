from mpi4py import MPI
import itertools

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
rank = comm.Get_rank()

#takes in a func and list and filters the list based on func through distributed programming
#assumes that the list size >= the number of processes
def distrib_filter(func, list_data):
	if rank == 0:
	    data = []
	    num_per_list = len(list_data)//nprocs
	    remainder = len(list_data)%nprocs
	    for x in range(nprocs):
	    	data.append(list_data[x*num_per_list:(x+1)*num_per_list])
	else:
		data = []
	data = comm.scatter(data, root=0)
	new_data = []
	for i in range(len(data)):
		item = func(data[i])
		if item:
			new_data.append(item)

	#Gather
	final_data = comm.gather(new_data, root=0)
	if rank == 0 and remainder > 0 :
		lastList = []
		for j in range(nprocs*num_per_list,len(list_data)):
			item = func(list_data[j])
			if item:
				lastList.append(item)
		final_data.append(lastList)

	comm.Barrier()
	if rank == 0 and final_data != None:
		return list(itertools.chain.from_iterable(final_data))

def square(x):
	return x*x

print(distrib_filter(square, [0,1,2,3,4,5,6,7,8,9,10,11,12,13]))

