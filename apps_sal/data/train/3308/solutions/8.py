def parity_bit(b):
    return ' '.join((s[:-1] if int(s[-1:]) == s[:-1].count('1') % 2 else 'error' for s in b.split()))
