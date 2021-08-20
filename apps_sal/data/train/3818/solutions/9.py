def get_mixed_num(fraction):
    (n, d) = map(int, fraction.split('/'))
    (i, n, d) = (n // d, n % d, d)
    return ['', f'{i} '][bool(i)] + f'{n}/{d}'
