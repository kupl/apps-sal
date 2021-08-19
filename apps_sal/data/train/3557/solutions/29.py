"""Large inputs are given because if you use a list comprehension iteration approach"""


def odd_count(n):
    return (n - 1) / 2 if n % 2 != 0 else n / 2
