def parity_bit(binary):
    return ' '.join((byte[:-1] if byte.count('1') % 2 == 0 else 'error' for byte in binary.split()))
