l, m, p = [1], 10 ** 7, []
for n in range(2, int(m ** .5) + 1):
    l = [n*n + j for j in [0]+l]
    p += [int(k) for k in map(str, l[1:]) if k == k[::-1]]
p = sorted(set(p))

from bisect import bisect_left
def values(n): return bisect_left(p, n)
