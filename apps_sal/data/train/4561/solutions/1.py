def solve(st):
    return all(abs(ord(x) - ord(y)) in {0, 2} for x, y in zip(st, st[::-1]))
