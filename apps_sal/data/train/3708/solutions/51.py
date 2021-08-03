hex_vals = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def hex_to_dec(s):
    accum = 0

    for pos, num in enumerate(reversed(s)):
        if num in '0123456789':
            accum += int(num) * (16**pos)
        else:
            accum += hex_vals[num] * (16**pos)

    return accum
