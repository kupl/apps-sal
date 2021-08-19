from itertools import permutations


def ssc_forperm(arr):
    lst = [sum((n * (i + 1) for (i, n) in enumerate(p))) for p in set(permutations(arr))]
    return [{'total perm': len(lst)}, {'total ssc': sum(lst)}, {'max ssc': max(lst)}, {'min ssc': min(lst)}]
