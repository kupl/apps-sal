def get_mixed_num(fraction):
    (a, b) = map(int, fraction.split('/'))
    (q, r) = divmod(a, b)
    return f'{q} {r}/{b}'
