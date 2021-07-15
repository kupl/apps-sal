def f(n):
    if type(n) == float or type(n) == str or n == 0 or n <= -1:
        return None
    else:
        return sum([elem for elem in range(0, n + 1)])
