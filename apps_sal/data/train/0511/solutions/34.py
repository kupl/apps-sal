import numpy as np
from numpy import int64

f = open(0)
N = int(f.readline())
a = np.fromstring(f.readline(), dtype=int64, sep=' ')
z = np.bitwise_xor.reduce(a)
ans = np.bitwise_xor(a, z)
print(*ans.tolist())
