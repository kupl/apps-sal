from itertools import permutations


def max_number(n):
    return max([int(''.join(i)) for i in permutations(list(str(n)))])
