def solve(st):
    return all(True if ord(x) - ord(y) in [-2, 0, 2] else False for x, y in zip(st, st[::-1]))
