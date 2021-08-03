from collections import defaultdict


def array_info(arr):
    d = defaultdict(int)
    for v in arr:
        d[type(v)] += 1
        d[' '] += v == ' '
    if not arr:
        return 'Nothing in the array!'
    return [[x or None] for x in (len(arr), d[int], d[float], d[str] - d[' '], d[' '])]
