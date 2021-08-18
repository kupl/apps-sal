def f(n):
    if (n == 0):
        return 1
    else:
        return n * f(n - 1) + (1 if n % 2 == 0 else -1)


def all_permuted(array_length):
    return f(array_length)
