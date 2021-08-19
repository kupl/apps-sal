def solve(a):
    a = [i for i in a if isinstance(i, int)]
    return sum((1 for i in a if i % 2 == 0)) - sum((1 for i in a if i % 2))
