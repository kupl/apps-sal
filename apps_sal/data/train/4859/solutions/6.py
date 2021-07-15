from itertools import permutations

def ssc_forperm(lst):
    scores = [sum(i*n for i, n in enumerate(p, 1)) for p in set(permutations(lst))]
    return [{"total perm": len(scores)}, {"total ssc": sum(scores)}, {"max ssc": max(scores)}, {"min ssc": min(scores)}]

