def f(n):
    try:
        return sum(range(n + 1)) if sum(range(n + 1)) else None
    except:
        return None
