from collections import Counter


def solve(files):
    extensions = Counter(['.' + i.split('.')[-1] for i in files])
    m = max(extensions.values(), default=0)
    return sorted([i for (i, j) in extensions.items() if j == m])
