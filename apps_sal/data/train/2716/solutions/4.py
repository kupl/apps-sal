a = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
b = ('a', 'e', 'i', 'o', 'u')


def encode(st):
    return ''.join((a[c] if c in a else c for c in st))


def decode(st):
    return ''.join((b[int(c) - 1] if c.isdigit() else c for c in st))
