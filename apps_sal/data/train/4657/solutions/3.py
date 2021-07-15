from itertools import permutations

def sort_by_perfsq(a):
    return [x for _, x in sorted([(-sum(1 for c in set(permutations(str(n))) if (float(''.join(c)) ** 0.5).is_integer()), n) for n in a])]
