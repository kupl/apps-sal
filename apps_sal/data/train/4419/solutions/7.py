from itertools import product
from collections import Counter

def reg_sum_hits(n, s):
    return sorted([[k, v] for k, v in Counter(sum(p) for p in product(*[[i for i in range(1, s+1)] for _ in range(n)])).items()])
