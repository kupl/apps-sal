def b2i(b):
    return sum((1 << i for (i, x) in enumerate(b[::-1]) if x == '1'))


def add(a, b):
    return format(b2i(a) + b2i(b), 'b')
