from collections import defaultdict
SQUARES = [x ** 2 for x in range(1, 3163)]
DIGITS = defaultdict(int)
for sqr in SQUARES:
    DIGITS[''.join(sorted(str(sqr)))] += 1


def sort_by_perfsq(arr):
    return sorted(arr, key=lambda n: (-DIGITS[''.join(sorted(str(n)))], n))
