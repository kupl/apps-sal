def f(n):
    if type(n) is not int or n <= 0:
        result = None
    else:
        lst = [i for i in range(0, n + 1)]
        result = sum(lst)
    return result
