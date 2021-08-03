def f(n):
    sum = 0
    if type(n) == int:
        if n <= 0:
            return None
        for x in range(n + 1):
            sum = sum + x
        return sum
    else:
        return None
    pass
