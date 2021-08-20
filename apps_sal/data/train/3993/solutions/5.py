def solve(a):
    return sum(((-1) ** x for x in a if isinstance(x, int)))
