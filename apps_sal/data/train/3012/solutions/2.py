def shared_bits(a, b):
    num = a & b
    count = bin(num).count("1")
    if count >= 2:
        return True
    return False
