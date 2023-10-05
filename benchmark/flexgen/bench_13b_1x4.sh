#!/bin/bash

MY_IPADDR=$(hostname -i)
all_hosts=$MY_IPADDR
N_GPUS=4
N_CORES_PER_GPU=6

PYTHON_EXEC=/opt/conda/bin/python
PYTHON_SCRIPT=flexgen.dist_flex_opt

pgrep -fl python | awk '!/dist_flex_opt\.py/{print $1}' | xargs kill

set -x

mpirun \
  --allow-run-as-root \
  --mca btl_tcp_if_exclude lo,docker0 \
  --mca oob_tcp_if_exclude lo,docker0 \
  --map-by ppr:$N_GPUS:node:pe=$N_CORES_PER_GPU --oversubscribe -H $all_hosts \
  --bind-to core -x OMP_NUM_THREADS=$N_CORES_PER_GPU \
  $PYTHON_EXEC -m $PYTHON_SCRIPT \
    --head-ip $MY_IPADDR \
    --port 7777 \
    --use-mpi \
    --model facebook/opt-13b \
    --gpu-batch-size 12 \
    --num-gpu-batches 1 \
    --percent 100 0 100 0 100 0 \
    --comm-device cpu \
    --overlap False \
    --compress-weight \
    --compress-cache \
    --compress-hidden \

#    --async-comm \