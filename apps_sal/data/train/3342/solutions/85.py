def pattern(n):
    a = ''
    for x in range(1, n + 1):
        a = a + str(x) * x + '\n'
    return a.rstrip('\n')
