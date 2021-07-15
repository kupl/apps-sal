def f(n):
    tot = 0
    if type(n) == int and n > 0:
        for number in range(1, n + 1):
            tot += number
        return tot
    return None
