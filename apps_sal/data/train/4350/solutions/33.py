def pre_fizz(n):
    n = list(range(n))
    x = n[-1] + 1
    n.append(x)
    del n[0]
    return n
