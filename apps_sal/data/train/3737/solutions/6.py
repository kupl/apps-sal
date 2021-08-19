def fifth(i, x):
    return x if i % 5 else -x


def third(i, x):
    return x if i % 3 else 3 * x


def square(x):
    return x if x < 0 else x * x


def calc(a):
    return sum((fifth(i, third(i, square(x))) for (i, x) in enumerate(a, 1)))
