#!/bin/bash

MY_IPADDR=$(hostname -i)
all_hosts=$MY_IPADDR
N_GPUS=2
N_CORES_PER_GPU=4
PYTHON_EXEC=/opt/conda/bin/python
PYTHON_SCRIPT=flexgen.dist_flex_opt

set -x

mpirun \
  --allow-run-as-root \
  --mca btl_tcp_if_exclude lo,docker0 \
  --mca oob_tcp_if_exclude lo,docker0 \
  --map-by ppr:2:node:pe=4 --oversubscribe -H $(hostname -i) \
  --bind-to core -x OMP_NUM_THREADS=4 \
  $PYTHON_EXEC -m $PYTHON_SCRIPT \
    --head-ip $(hostname -i) \
    --port 7777 \
    --use-mpi \
    --model facebook/opt-1.3b \
    --gpu-batch-size 16 \
    --num-gpu-batches 3 \
    --percent 0 100 0 100 100 0 \
    --comm-device cpu \
    --cut-gen-len 5 \
    --path _DUMMY_
