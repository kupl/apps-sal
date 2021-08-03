from collections import Counter
from itertools import combinations


def ulam_sequence(u0, u1, n):
    seq = [u0, u1]
    for i in range(n - 2):
        c = Counter(a + b for a, b in combinations(seq, 2))
        x = min(key for key in c if key > seq[-1] and c[key] == 1)
        seq.append(x)
    return seq
