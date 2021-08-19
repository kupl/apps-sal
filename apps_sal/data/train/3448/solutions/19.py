def f(n):
    try:
        if n > 0 and type(n) is int:
            return int(n * (n + 1) / 2)
    except:
        return None
