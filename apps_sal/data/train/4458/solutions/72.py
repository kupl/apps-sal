def time_correct(t):
    return t if not t else '{:02d}:{:02d}:{:02d}'.format(*(lambda q: [q // 3600 % 24, q % 3600 // 60, q % 60])(sum([a * b for (a, b) in zip([3600, 60, 1], map(int, t.split(':')))]))) if __import__('re').match('^\\d\\d:\\d\\d:\\d\\d$', t) else None
