####    Use MPI for communication with Horovod
export HOROVOD_GPU_ALLREDUCE=MPI
export HOROVOD_GPU_ALLGATHER=MPI
export HOROVOD_GPU_BROADCAST=MPI

horovodrun -np 2 -H localhost:2 python horovod_test.py