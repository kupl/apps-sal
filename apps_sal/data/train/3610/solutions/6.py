def fixed_xor(a, b):
    return ''.join(list(map(lambda x: format(int(x[0], 16) ^ int(x[1], 16), 'x'), zip(a, b))))
