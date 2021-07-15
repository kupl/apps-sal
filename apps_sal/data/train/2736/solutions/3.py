from itertools import permutations
def largest_arrangement(numbers):
    return int(max(("".join(r) for r in permutations(list(map(str,numbers)))), key = int))

