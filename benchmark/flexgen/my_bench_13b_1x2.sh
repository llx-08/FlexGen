#!/bin/bash

MY_IPADDR=$(hostname -i)
all_hosts=$MY_IPADDR
N_GPUS=2
N_CORES_PER_GPU=4

PYTHON_SCRIPT=flexgen.dist_flex_opt

set -x

mpirun \
  --allow-run-as-root
  --mca btl_tcp_if_exclude lo,docker0 \
  --mca oob_tcp_if_exclude lo,docker0 \
  --map-by ppr:2:node:pe=4 --oversubscribe -H $(hostname -i) \
  --bind-to core -x OMP_NUM_THREADS=4 \
  /opt/conda/bin/python -m /opt/conda/bin/python \
    --head-ip $(hostname -i) \
    --port 7777 \
    --use-mpi \
    --model facebook/opt-13b \
    --gpu-batch-size 24 \
    --percent 100 0 100 0 100 0 \
    --comm-device cpu \
    --cut-gen-len 5 \
    --path _DUMMY_
