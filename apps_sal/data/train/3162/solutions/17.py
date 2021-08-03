def f(x): return sum([ord(y) for y in list(x.upper())]) if x and x.isalpha() else 0


def compare(s1, s2):
    return f(s1) == f(s2)
