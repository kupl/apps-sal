def operation(a, b):
    res = 0
    while a != 1 << a.bit_length() - 1:
        (a, res) = (a >> 1, res + 1)
    return res + abs(a.bit_length() - b.bit_length())
