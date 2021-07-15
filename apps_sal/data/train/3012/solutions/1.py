def shared_bits(a, b):
    return bool(a & b & (a & b) - 1)
