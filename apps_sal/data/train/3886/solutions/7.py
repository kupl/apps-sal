import itertools
import numpy as np

s = np.ones(100000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0


def total(arr):
    return sum(itertools.compress(arr, s))
