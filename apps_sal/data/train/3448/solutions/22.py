def f(n):
    if type(n)!=int:
        return None
    return sum([x for x in range(n+1)]) if n>0 else None
