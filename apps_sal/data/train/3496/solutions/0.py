def sort_by_area(seq):
    def func(x):
        if isinstance(x, tuple):
            return x[0] * x[1]
        else:
            return 3.14 * x * x
    return sorted(seq, key=func)
