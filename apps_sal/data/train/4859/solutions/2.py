def ssc_forperm(arr):
    from itertools import permutations, count, imap
    from operator import mul
    perms = list(set(permutations(arr)))
    scc = [sum(imap(mul, i, count(1))) for i in perms]
    return [{'total perm': len(scc)}, {'total ssc': sum(scc)}, {'max ssc': max(scc)}, {'min ssc': min(scc)}]
