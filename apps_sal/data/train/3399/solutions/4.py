def alpha_seq(string):
    o = ord('a') - 1
    return ','.join(((c * (ord(c) - o)).capitalize() for c in sorted(string.lower())))
