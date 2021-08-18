def past(h, m, s):
    res = int(str(h * 36) + '00000') + int(str(m * 6) + '0000') + int(str(s) + '000')
    return res
