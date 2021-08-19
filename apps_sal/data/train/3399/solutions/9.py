def alpha_seq(s):
    return ','.join((c.upper() + c * (ord(c) - 97) for c in sorted(s.lower())))
