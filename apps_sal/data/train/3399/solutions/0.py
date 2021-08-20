def alpha_seq(s):
    return ','.join(((c * (ord(c) - 96)).capitalize() for c in sorted(s.lower())))
