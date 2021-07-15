def alpha_seq(string):
    return ','.join(a * (ord(a) - 96) for a in sorted(string.lower())).title()
