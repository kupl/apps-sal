def f(n):
    try:
        int(n)
        if n <= 0:
            return None
        else:
            return sum(range(n + 1))
    except:
        return None
