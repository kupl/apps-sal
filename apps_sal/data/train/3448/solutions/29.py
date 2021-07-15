def f(n):
    if type(n)==int and n>0:
        return sum([x for x in range(n+1)])
    else:
        return None
