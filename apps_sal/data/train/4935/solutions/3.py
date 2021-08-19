def infected(s):
    inf = 0
    saf = 0
    for c in s.split('X'):
        if '1' in c:
            inf += len(c)
        else:
            saf += len(c)
    return 0 if inf + saf == 0 else inf / (inf + saf) * 100
