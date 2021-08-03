def f(n):
    if type(n) == int and n > 0:
        num = 0
        for i in range(n + 1):
            num += i
        return num
