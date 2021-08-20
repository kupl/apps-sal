from itertools import combinations
from collections import defaultdict


def ulam_sequence(u0, u1, n):
    seq = [u0, u1, u0 + u1]
    while len(seq) < n:
        candidates = defaultdict(int)
        for (a, b) in combinations(seq, 2):
            candidates[a + b] += 1
        for (num, pairs) in sorted(candidates.items()):
            if num > seq[-1] and pairs == 1:
                seq.append(num)
                break
    return seq
