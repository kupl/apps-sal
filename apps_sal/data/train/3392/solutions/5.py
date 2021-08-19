def sierpinski(n):
    if n == 0:
        return '*'
    s = sierpinski(n - 1).split('\n')
    ss = []
    for i in range(2 ** n // 2):
        ss.append(s[i].center(2 ** n * 2 - 1))
    for i in range(2 ** n // 2):
        ss.append(s[i] + ' ' + s[i])
    return '\n'.join(ss)
