def pattern(n):
    a = ''
    lst = []
    result = ''
    for i in range(1, n + 1):
        a = str(i)
        for m in range(i + 1, n + 1):
            a += str(m)
        lst.append(a)
    for i in lst:
        result += i + '\n'
    return result[:-1]
