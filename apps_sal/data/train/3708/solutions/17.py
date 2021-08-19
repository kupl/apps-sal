def hex_to_dec(s):
    (result, count) = (0, 0)
    hexes = '0123456789ABCDEF'
    s_r = s.upper()[::-1]
    for i in s_r:
        result += hexes.find(i) * 16 ** count
        count += 1
    return result
