def commas(num):
    n = format(round(num, 3), ",").split('.')
    return n[0] + '.' + n[1] if len(n) > 1 and n[1] != '0' else n[0]
