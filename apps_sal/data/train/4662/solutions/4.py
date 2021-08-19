import numpy as np
s = np.ones(100000)
s[1] = s[4::2] = 0
for i in range(3, int(len(s) ** 0.5) + 1, 2):
    if not s[i]:
        continue
    s[i * i::i] = 0
PRIME_DIGITS = {'2', '3', '5', '7'}
the_array = [i for (i, x) in enumerate(s) if not x and PRIME_DIGITS.isdisjoint(str(i))]


def solve(n):
    return the_array[n]
