def hex_to_dec(s):
    m = '0123456789ABCDEF'
    result = 0
    for i in range(0, len(s)):
        result += m.index(s[i].upper()) * 16 ** (len(s) - 1 - i)
    return result
