from itertools import starmap, combinations
from operator import lt, gt


def longest_comb(arr, command):
    check = lt if command.startswith('<') else gt
    for i in range(len(arr), 2, -1):
        result = [list(x) for x in combinations(arr, i) if all(starmap(check, zip(x, x[1:])))]
        if result:
            return result[0] if len(result) == 1 else result
    return []
