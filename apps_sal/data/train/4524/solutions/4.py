from itertools import permutations

def permutation_average(n):
  perms = [float(''.join(x)) for x in permutations(str(n))]
  return round(sum(perms) / len(perms))
