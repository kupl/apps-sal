def number_property(n):
    return [n == 2 or n > 2 and pow(2, n - 1, n) == 1,
            not n % 2,
            not n % 10]
