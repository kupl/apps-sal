from operator import add, mul


def array_conversion(a):
    i, f = 1, [mul, add]
    while len(a) > 1:
        a = [f[i](x, y) for x, y in zip(a[::2], a[1::2])]
        i ^= 1
    return a[0]
