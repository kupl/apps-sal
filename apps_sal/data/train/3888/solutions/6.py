def clock_degree(s):
    return (lambda h, m: '%s:%s' % (30 * (h % 12) or 360, 6 * m or 360) if 0 <= h <= 23 and 0 <= m <= 59 else 'Check your time !')(*[int(a) for a in s.split(':')])
