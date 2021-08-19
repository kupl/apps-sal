def f(s):
    return isinstance(s, str) and s.isalpha() and sum(map(ord, s.upper()))


def compare(a, b):
    return f(a) == f(b)
