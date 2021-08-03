def alpha_seq(s): return ','.join(e.upper() + e * (ord(e) - 97) for e in sorted(s.lower()))
