def multiply(n):
    return n * 5 ** number_of_digits(n)


def number_of_digits(n: int):
    return 1 if -10 < n < 10 else 1 + number_of_digits(n // 10)
