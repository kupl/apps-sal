def fixed_xor(a, b):
    return "".join(format(int(x, 16) ^ int(y, 16), "x") for x, y in zip(a, b))
