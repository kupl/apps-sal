def consecutive_ducks(n):
    return n != 1 << n.bit_length()-1
