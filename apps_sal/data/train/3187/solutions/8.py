def sum_nested(L):
    return sum(x if isinstance(x, int) else sum_nested(x) for x in L)
