def mid_endian(n):
    x = format(n, 'X')
    xs = [a+b for a, b in zip(*[iter('0' * (len(x) % 2) + x)]*2)]
    return ''.join(xs[1::2][::-1] + xs[::2])
