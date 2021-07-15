def shared_bits(a, b):
    return a & b and bin(a & b).count("1") > 1
