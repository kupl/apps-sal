from functools import reduce

def trouble(x, t):
    return reduce(lambda a, u: a + ([u] if not a or a[-1] + u != t else []), x[1:], x[0:1])
