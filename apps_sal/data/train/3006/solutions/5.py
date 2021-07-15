from functools import reduce

def calculate_total(t1, t2):
    f = lambda t: reduce(lambda a, b: a + b, t, 0)
    return f(t1) > f(t2)
