def f(n):
    x = []
    if type(n) == int and int(n) > 0:
        n = abs(n)
        for i in range(1, n + 1):
            x.append(i)
        return (sum(x))
    else:
        return None
