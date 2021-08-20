def Dragon(n):
    if type(n) != type(1):
        return ''
    if n < 0:
        return ''
    if n == 0:
        return 'F'
    ret = 'Fa'
    while n > 0:
        temp = ''
        for word in ret:
            if word == 'a':
                temp += 'aRbFR'
            elif word == 'b':
                temp += 'LFaLb'
            else:
                temp += word
        ret = temp
        n -= 1
    ret = ret.replace('a', '')
    ret = ret.replace('b', '')
    return ret
