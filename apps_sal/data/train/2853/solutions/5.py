def solve(l):
    return sorted(set(l), key=l[::-1].index)[::-1]
