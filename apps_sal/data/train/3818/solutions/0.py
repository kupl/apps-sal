def get_mixed_num(fraction):
    n, d = [int(i) for i in fraction.split('/')]
    return '{} {}/{}'.format(n // d, n % d, d)
