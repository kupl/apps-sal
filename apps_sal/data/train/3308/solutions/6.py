def parity_bit(binary):
    return ' '.join(('error' if a.count('1') % 2 else a[:-1] for a in binary.split()))
