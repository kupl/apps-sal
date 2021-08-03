def f(n):
    if type(n) == int:
        if n > 0:
            return sum(range(n + 1))
    else:
        return None
