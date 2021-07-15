from itertools import permutations

def permutation_average(n):
    perms = [float(''.join(e)) for e in permutations(str(n))]
    return int(round(sum(perms) / len(perms)))

