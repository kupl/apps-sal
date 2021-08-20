def time(d, v, s):
    return round(d / (v + int(s.split()[1]) * (1 if s[0] == 'D' else -1)), 2)
