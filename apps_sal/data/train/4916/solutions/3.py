from itertools import compress, islice, zip_longest

import numpy as np


s = np.ones(1000000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5)+1, 2):
    if s[i]:
        s[i*i::i] = 0
primes = list(compress(range(len(s)), s))

def get_primes(how_many, group_size=2):
    yield from zip_longest(*[islice(primes, how_many)] * group_size)
