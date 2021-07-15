def elongate(c):
    u = c.upper()
    return '{0}{1}'.format(u, c.lower()*(ord(u)-65))
    
def alpha_seq(s):
    return ','.join(sorted([elongate(c) for c in s]))
