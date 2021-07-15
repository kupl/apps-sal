def pattern(n):
    print(n)
    if n <= 0:
        return ''
    s = '1'
    for i in range(2,n+1):
        s += '\n' + i*str(i)
    return s
