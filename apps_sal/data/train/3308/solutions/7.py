def parity_bit(s):
    return ' '.join('error' if x.count('1') % 2 else x[:-1] for x in s.split())
