def convert_to_mixed_numeral(parm):
    (n, d) = list(map(int, parm.split('/')))
    sign = '-' if n < 0 else ''
    (m, n) = divmod(abs(n), d)
    return parm if m == 0 else sign + f'{m}' + f' {n}/{d}' * (n != 0)
