import os
import torch.distributed as dist
import torch
import multiprocessing as mp

print(f'Initializing distributed environment at {"172.17.0.3"}:{7777}, '
      f'world_size={2}, rank={1}, local_rank={1}.')

# Initialize distributed environment
torch.cuda.set_device(1)
distributed_init_method = f'tcp://{"172.17.0.3"}:{7777}'
global _COMM_DEVICE

backend = 'gloo'
# backend = 'nccl'

# rank 进程序号， local_rank GPU编号
dist.init_process_group(backend=backend,
                        init_method=distributed_init_method,
                        world_size=2,
                        rank=1)

# Create groups for pipeline parallelism
global _PIPELINE_PARALLEL_PRED_GROUP, _PIPELINE_PARALLEL_SUCC_GROUP

for pred in range(2):
    succ = (pred + 1) % 2
    group = dist.new_group([pred, succ])
    if pred == 1:
        _PIPELINE_PARALLEL_PRED_GROUP = group
    if succ == 1:
        _PIPELINE_PARALLEL_SUCC_GROUP = group

print("Finished initializing distributed environment")

a = torch.ones(1).to('cuda:0')
dist.all_reduce(a)
print(a.item())
