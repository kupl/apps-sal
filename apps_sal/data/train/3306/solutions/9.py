def solve(a, b):
    return a == b or ('*' in a and (lambda l: not l[0] == l[1] == b and b.startswith(l[0]) and b.endswith(l[1]))(a.split('*')))
