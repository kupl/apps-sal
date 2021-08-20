from itertools import permutations
from math import sqrt


def is_per(n):
    return str(sqrt(int(n)))[-1] == '0'


def next_perfectsq_perm(lower_limit, k):
    perfect = [i ** 2 for i in range(2000) if '0' not in str(i ** 2) if i ** 2 > lower_limit]
    for i in perfect:
        if i > lower_limit:
            num = set()
            per = set(permutations(str(i)))
            tem = [int(''.join(j)) for j in per if is_per(''.join(j))]
            if len(tem) == k:
                num.add(i)
                ma = max(tem)
                break
    return max(tem)
