from math import ceil, floor

def round_it(n):
    s = str(n).split('.')
    return ceil(n) if len(s[0]) < len(s[1]) else floor(n) if len(s[0]) > len(s[1]) else round(n)
