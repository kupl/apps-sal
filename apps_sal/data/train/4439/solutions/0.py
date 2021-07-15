import numpy as np
s = np.ones(100000)
for i in range(2, 100000):
    s[i::i] += 1

def div_num(a, b):
    return max(range(a, b+1), key=lambda i: (s[i], -i), default='Error')
