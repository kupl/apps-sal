def padovan(n):
    a = b = c = 1
    for i in range(n // 3):
        a += b
        b += c
        c += a
    return (a, b, c)[n % 3]
