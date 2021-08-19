def hex_to_dec(s):
    d = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    res = 0
    for i in s:
        res *= 16
        if i.isdigit():
            res += int(i)
        else:
            res += d.get(i)
    return res
