def string_expansion(s):
    dec = 1
    ret = ''
    for e in s:
        dec = {0: dec, 1: e}[e.isdigit()]
        ret += ['', e * int(dec)][e.isalpha()]
    return ret
