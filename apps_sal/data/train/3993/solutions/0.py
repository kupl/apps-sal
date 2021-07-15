def solve(a):
    return sum(1 if v % 2 == 0 else -1 for v in a if type(v) == int)
