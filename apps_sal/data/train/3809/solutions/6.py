def charCheck(text, mx, spaces):
    stringa = ''
    limit = False
    result = ''
    limit_val = 0
    if spaces:
        stringa = text
    else:
        stringa = text.replace(' ', '')
    limit_val = mx - len(stringa)
    if limit_val >= 0:
        limit = True
        limit_val = len(stringa)
    else:
        limit_val = mx
    for i in range(limit_val):
        result += stringa[i]
    return [limit, result]
