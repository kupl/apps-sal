from itertools import permutations


def permutation_average(n):
    a = [int("".join(x)) for x in set(permutations(str(n)))]
    return round(float(sum(a)) / len(a))
