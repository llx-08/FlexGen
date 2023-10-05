import torch
import numpy as np

b = 16
s = 512
h = 512
dst_tensor = torch.ones((b, s, h), dtype=torch.int8, pin_memory=True)

dst_indices = (slice(0, b), slice(0, s), slice(0, h))

a = [(x.stop - x.start) / (x.step or 1) for x in dst_indices]


size = np.prod(a)

print(dst_indices)
print(a)
print(size)

import torch

a = torch.zeros([1, 1], dtype=torch.float32)
print(a.element_size() * a.nelement())

a = torch.zeros([7, 512, 5120], dtype=torch.float32)
print(a.element_size() * a.nelement())

print(1 << 20)
print(2**20)

print(73400320/7 /7.145 / (1<<30))