from itertools import permutations
def largest_arrangement(numbers):
    return int(max(''.join(xs) for xs in permutations(map(str, numbers))))
