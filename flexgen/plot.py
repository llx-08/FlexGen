import matplotlib.pyplot as plt

import numpy as np

# single batch token time
token_time = [5.85, 2.8954384652897716, 2.9097139071673155, 2.9048069803975523, 2.506138315424323]

plt.plot(np.arange(len(token_time)), token_time)
plt.show()

# multibatch throughput: gpu_batch_size = 2

gpu_batch_num = np.arange(1, 8)
throughput = [1.48, ]

decode_token = [[2.8280230998061597, 2.835507918149233, 2.826319829095155, 2.465744319371879],
                [2.912149203941226, 2.9241559891961515, 2.921957320999354, 2.5528810461983085]

                ]

prefill_token = [3.94]