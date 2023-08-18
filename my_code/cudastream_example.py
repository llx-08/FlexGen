import time

import torch

# 创建CUDA流
stream = torch.cuda.Stream()

t = time.time()
# 在流中执行操作
with torch.cuda.stream(stream):
    # 创建CUDA张量
    a = torch.randn(1000, 1000, device='cuda')
    b = torch.randn(1000, 1000, device='cuda')

    # 执行矩阵乘法操作
    c = torch.matmul(a, b)

# 等待流中的操作完成
torch.cuda.synchronize()

# 在默认流中执行其他操作
d = torch.randn(1000, 1000, device='cuda')
e = torch.matmul(c, d)

t_ = time.time()

print(t_-t)

# # without cudastream
# t = time.time()
#
# a = torch.randn(1000, 1000, device='cuda')
# b = torch.randn(1000, 1000, device='cuda')
#
# # 执行矩阵乘法操作
# c = torch.matmul(a, b)
#
# d = torch.randn(1000, 1000, device='cuda')
# e = torch.matmul(c, d)
# t_ = time.time()
# print(t_-t)
