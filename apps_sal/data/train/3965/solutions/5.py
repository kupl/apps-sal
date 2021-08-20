def powerof4(n):
    return type(n) == int and n.bit_length() & 1 and (n == 1 << n.bit_length() - 1)
