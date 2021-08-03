from itertools import islice


def count_inversions(array):
    return sum(
        sum(x > y for y in islice(array, i + 1, None))
        for i, x in enumerate(array)
    )
