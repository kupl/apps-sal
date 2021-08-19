def get_mixed_num(fraction):
    (n, d) = (int(num) for num in fraction.split('/'))
    (i, n) = divmod(n, d)
    return f'{i} {n}/{d}'
