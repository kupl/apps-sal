from itertools import permutations


def largest_arrangement(numbers):
    return max((int(''.join(p)) for p in permutations(map(str, numbers))))
