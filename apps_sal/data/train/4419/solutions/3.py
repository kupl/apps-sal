from collections import Counter
from itertools import product

def reg_sum_hits(n,s):
    return list(map(list,sorted(Counter(map(sum,product(range(1,s+1),repeat=n))).items())))
