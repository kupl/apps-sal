def get_mixed_num(fraction):
    (a, b) = list(map(int, fraction.split('/')))
    return '{} {}/{}'.format(a // b, a % b, b)
