def add_binary(a, b):
    if type(a) == str and type(b) == str:
        res = bin(int(a, 2) + int(b, 2))
    else:
        res = bin(a + b)
    return res[2:]
