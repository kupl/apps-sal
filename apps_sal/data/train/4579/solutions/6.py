def pattern(n):
    if n < 1:
        return ''
    res = []
    current = str(n)[-1]
    strng = ''
    res.append(current * n)
    for i in range(1, n):
        strng = (strng + current)
        if current == '0':
            res.append(strng.ljust(n, '9'))
            current = '9'
        else:
            res.append(strng.ljust(n, str(int(current) - 1)))
            current = str(int(current) - 1)
    return '\n'.join(res)
