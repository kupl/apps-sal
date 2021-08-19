def add_binary(a, b):
    c = a + b
    l = []
    if c < 0:
        return '-' + dec2bin(abs(c))
    while True:
        (c, remainder) = divmod(c, 2)
        l.append(str(remainder))
        if c == 0:
            return ''.join(l[::-1])
