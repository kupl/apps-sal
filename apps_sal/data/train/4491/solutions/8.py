def solve(a, b):
    return a.translate(str.maketrans('', '', b)) + b.translate(str.maketrans('', '', a))
