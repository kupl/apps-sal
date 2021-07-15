def clock_degree(s) :
    h, m = map(int, s.split(':'))
    if not (0 <= h < 24 and 0 <= m < 60): return "Check your time !"
    return "{}:{}".format((h%12) * 30 or '360', m * 6 or '360')
