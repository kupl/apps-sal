def hex_to_dec(s):
    a = 0
    dic_hex = {'a': 10,
               'b': 11,
               'c': 12,
               'd': 13,
               'e': 14,
               'f': 15}
    for i in range(0, len(s)):
        print(s[-(i + 1)], i)
        a += int(dic_hex.get(s[-(i + 1)], s[-(i + 1)])) * 16 ** i
    return a
