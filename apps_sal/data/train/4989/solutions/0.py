def hollow_triangle(n):
    width = n * 2 - 1
    row = '{{:_^{}}}'.format(width).format
    return [row(mid(a)) for a in xrange(1, width, 2)] + [width * '


def mid(n):
    return '
