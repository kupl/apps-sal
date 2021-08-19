def f(n):
    if isinstance(n, int) != True or n <= 0:
        return None
    elif n == 1:
        return 1
    else:
        return (1 + n) * (n / 2)
