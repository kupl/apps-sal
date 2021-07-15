def f(n):
    if type(n) == str or type(n) == float or n < 1:
        return None
    return sum(range(1, n+1))
