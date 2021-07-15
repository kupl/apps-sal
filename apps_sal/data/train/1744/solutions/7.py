def fusc(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in map(int, reversed(f'{n-1:b}')):
        if i:
            b += a
        else:
            a += b
    return b
