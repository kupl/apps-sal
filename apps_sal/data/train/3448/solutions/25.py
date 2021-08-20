def f(n):
    try:
        if n % 1 == 0 and n > 0:
            return sum(range(0, n + 1, 1))
        else:
            return None
    except TypeError:
        return None
