def f(n):
    try:
        return None if n <= 0 else sum(range(1, (n + 1)))
    except:
        return None
