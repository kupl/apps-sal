def f(n):
    try:
        return n*(n+1)/2 if n>0 and (n - round(n) == 0) else None
    except TypeError:
        return None
