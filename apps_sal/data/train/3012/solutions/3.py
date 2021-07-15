def shared_bits(a, b):
    return len(bin(a&b).strip('0b0'))>1
