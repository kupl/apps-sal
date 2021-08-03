def hex_to_dec(s):
    exp = result = 0

    for i in s[::-1]:
        result += '0123456789abcdef'.index(i) * 16 ** exp
        exp += 1

    return result
