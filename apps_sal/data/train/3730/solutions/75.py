def capitalize(s):
    res = ''.join([s[i] if i % 2 else s[i].upper() for i in range(len(s))])
    return [res, res.swapcase()]
