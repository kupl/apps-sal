idx, n, seq = 2, 6, [1, 2, 4, 6]
while n < 2 ** 41:
    idx += 1
    seq.extend(range(n + idx, n + (seq[idx] - seq[idx-1]) * idx + 1, idx))
    n += (seq[idx] - seq[idx-1]) * idx

from bisect import bisect
def find(n): return bisect(seq, n)
