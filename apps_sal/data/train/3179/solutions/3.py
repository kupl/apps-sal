def min_and_max(l, d, x):
    def min_or_max(l, d, x, end, step):
        return next(i for i in range(l, d+end, step) if sum(map(int,list(str(i)))) == x)
    return [min_or_max(l, d, x, 1, 1), min_or_max(d, l, x, 0, -1)]
