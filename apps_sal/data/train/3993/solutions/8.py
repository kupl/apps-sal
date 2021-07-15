def solve(a):
    return sum(isinstance(x, int) and (1, -1)[x % 2] for x in a)
