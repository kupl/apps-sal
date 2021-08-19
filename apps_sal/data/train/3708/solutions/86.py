def hex_to_dec(s):
    h = '0123456789abcdef'
    y = len(s) - 1
    x = 0
    for i in s:
        print(i)
        x += h.index(i) * 16 ** y
        y -= 1
    return x
