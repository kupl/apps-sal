def add_binary(a, b):
    c = bin(int(a) + int(b))
    c = str(c)
    c = list(c)
    return ''.join(c[2:len(c) + 1])
