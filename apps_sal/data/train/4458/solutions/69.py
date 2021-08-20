def time_correct(t):
    if t is None:
        return None
    if t == '':
        return ''
    if len(t) < 8:
        return None
    count = 0
    for letter in t:
        if letter not in '0123456789:':
            return None
        if letter in '0123456789':
            count += 1
    if count > 6:
        return None
    x = int(t[-2:])
    y = int(t[3:5])
    z = int(t[:2])
    if x >= 60:
        x = x - 60
        y = y + 1
    if y >= 60:
        y = y - 60
        z = z + 1
    if z >= 24:
        z = z - z // 24 * 24
    if z <= 9:
        z = '0' + str(z)
    if y <= 9:
        y = '0' + str(y)
    if x <= 9:
        x = '0' + str(x)
    return str(z) + ':' + str(y) + ':' + str(x)
