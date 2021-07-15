from itertools import permutations
def ssc_forperm(arr):
    perms = set(p for p in permutations(arr))
    values = [sum((x + 1) * y for x,y in enumerate(i)) for i in perms]
    return [{"total perm": len(perms)}, {"total ssc": sum(values)}, {"max ssc": max(values)}, {"min ssc": min(values)}]
