def f(n):
    print('The number is' + str(n))
    if n == 1:
        return n
    if type(n) != int or n <= 0:
        return None
    return (n / 2) * (n + 1)
