from itertools import permutations
from collections import defaultdict


def rearranger(k, *args):
    (vals, D) = (map(str, args), defaultdict(set))
    for p in permutations(vals):
        x = int(''.join(p))
        if not x % k:
            D[x].add(p)
    try:
        mini = min(D)
        res = D[mini]
        return f"Rearrangement{('s' if len(res) > 1 else '')}: {' and '.join(map(', '.join, res))} generates: {mini} divisible by {k}"
    except:
        return 'There is no possible rearrangement'
