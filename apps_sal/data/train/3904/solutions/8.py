def is_divisible_by_6(s):
    return [] if s[-1] in '13579' else sum((is_divisible_by_6(s.replace('*', e, 1)) for e in '0123456789'), []) if s.count('*') > 1 else (lambda t: [s.replace('*', str(e)) for e in range((3 - t) % 3, 10, 3) if s[-1] != '*' or not e % 2])(sum((int(e) for e in s if e != '*')))
