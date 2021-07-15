import numpy as np

def ssloop(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(x*x for x in map(int, str(n)))
    return n == 1

s = np.ones(50001)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s) ** 0.5) + 1, 2):
    if s[i]:
        s[i*i::i] = 0
xs = [i for i, x in enumerate(s) if x and ssloop(i)]

def solve(a,b):
    return np.searchsorted(xs, b) - np.searchsorted(xs, a)
