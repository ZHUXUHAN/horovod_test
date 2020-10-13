####    Use MPI for communication with Horovod
#export HOROVOD_GPU_ALLREDUCE=MPI
#export HOROVOD_GPU_ALLGATHER=MPI
#export HOROVOD_GPU_BROADCAST=MPI

horovodrun -np 4 -H localhost:4 python horovod_mnist.py