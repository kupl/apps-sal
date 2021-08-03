from itertools import starmap, combinations
from operator import lt, gt


def longest_comb(arr, command):
    check = lt if command.startswith('<') else gt
    for i in range(len(arr), 2, -1):
        # if all(map(check, x, x[1:])) In Python 3
        result = [list(x) for x in combinations(arr, i) if all(starmap(check, zip(x, x[1:])))]
        # Also always annoying to return only the first element when we only have one
        if result:
            return result[0] if len(result) == 1 else result
    return []
