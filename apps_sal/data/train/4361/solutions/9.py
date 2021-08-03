import itertools


def next_perfectsq_perm(l, k):
    def perf(n): return n**0.5 % 1 == 0
    while True:
        l += 1
        if perf(l) and '0' not in str(l):
            r = [x for x in set([int(''.join(x)) for x in list(itertools.permutations(str(l)))]) if perf(x)]
            if len(r) == k:
                return max(r)
