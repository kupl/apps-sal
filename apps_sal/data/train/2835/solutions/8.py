import numpy as np

xs = np.ones(1000000)
xs[:2] = 0
xs[2*2::2] = 0
for i in range(3, len(xs), 2):
    if not xs[i]:
        continue
    xs[i*i::i] = 0
primes = [i for i, x in enumerate(xs) if x]
s = ''.join(c for p in primes for c in str(p))

def solve(a, b):
    return s[a:a+b]
