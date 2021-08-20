def value(x):
    x = x.split('.')
    return int(x[0]) * 256 ** 3 + int(x[1]) * 256 ** 2 + int(x[2]) * 256 + int(x[3])


def ips_between(start, end):
    return value(end) - value(start)
