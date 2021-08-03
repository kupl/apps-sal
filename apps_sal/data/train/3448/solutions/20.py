def f(n):
    if type(n) == int and n > 0:
        return (1 + n) * n / 2
    elif type(n) == str or type(n) == float or n < 0:
        return None
    else:
        return None
