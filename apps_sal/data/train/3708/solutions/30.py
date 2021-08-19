def hex_to_dec(s):
    inv = list(s)[::-1]
    arr = []
    for i in range(len(inv)):
        for j in range(10):
            if inv[i] == str(j):
                arr.append(j * 16 ** i)
        if inv[i] == 'a':
            arr.append(10 * 16 ** i)
        elif inv[i] == 'b':
            arr.append(11 * 16 ** i)
        elif inv[i] == 'c':
            arr.append(12 * 16 ** i)
        elif inv[i] == 'd':
            arr.append(13 * 16 ** i)
        elif inv[i] == 'e':
            arr.append(14 * 16 ** i)
        elif inv[i] == 'f':
            arr.append(15 * 16 ** i)
    res = 0
    for i in arr:
        res += i
    return res
