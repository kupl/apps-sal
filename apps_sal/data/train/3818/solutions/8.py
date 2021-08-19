def get_mixed_num(fraction):
    (n, d) = map(int, fraction.split('/'))
    (a, b) = divmod(n, d)
    return f'{a} {b}/{d}'
