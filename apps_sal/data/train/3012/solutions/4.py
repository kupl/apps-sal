def shared_bits(a, b):
    return f"{a & b:b}".count("1") > 1
