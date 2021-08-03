from collections import defaultdict


def group_in_10s(*args):
    d = defaultdict(list)
    for x in args:
        d[x // 10].append(x)
    return [sorted(d[k]) if k in d else None for k in range(0, max(d) + 1)] if d else []
