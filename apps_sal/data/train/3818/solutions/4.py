def get_mixed_num(f):
    v, d = map(int, f.split('/'))
    n, r = divmod(v, d)
    return f'{n} {r}/{d}'
