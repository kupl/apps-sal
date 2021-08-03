from itertools import permutations


def sort_by_perfsq(lst):
    return sorted(lst, key=perfsq)


def perfsq(n):
    perm = {int("".join(p)) for p in permutations(str(n))}
    return sum(-1 for n in perm if n**0.5 % 1 == 0), n
