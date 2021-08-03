def solve(st):
    return [all(ord(x) - ord(y) in [2, 0, -2] for x, y in zip(st, st[::-1]))][0]
