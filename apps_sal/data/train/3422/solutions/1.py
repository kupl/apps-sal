def diamond(n):
    w = ''
    space = n // 2
    starnum = 1
    while starnum < n:
        w += space * ' ' + starnum * '*' + '\n'
        starnum += 2
        space -= 1
    while starnum > 0:
        w += space * ' ' + starnum * '*' + '\n'
        starnum -= 2
        space += 1
    return w if n % 2 != 0 and n > 0 else None
