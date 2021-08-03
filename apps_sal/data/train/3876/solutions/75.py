def find(n):
    def x(b): return range(0, n + 1, b)
    return sum(set((*x(3), *x(5))))
