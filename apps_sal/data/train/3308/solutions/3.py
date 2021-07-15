def parity_bit(binary):
    res = ''
    for b in binary.split(' '):
        if b[:-1].count('1') % 2 == int(b[-1]):
            res += b[:-1] + ' '
        else:
            res += 'error '
    return res[:-1]
