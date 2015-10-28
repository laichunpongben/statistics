import numpy as np

samples = np.random.multinomial(100, [1/6.]*6, size=1000000)
max_x = [max(x) for x in samples]
print(np.mean(max_x))
