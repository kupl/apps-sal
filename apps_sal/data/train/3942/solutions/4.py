def solve(n):
    i = 0
    if str(n)[-1] != '0':
        return -1
    while n > 0:
        if n >= 500:
            i += 1
            n -= 500
        if n >= 200 and n < 500:
            i += 1
            n -= 200
        if n >= 100 and n < 200:
            i += 1
            n -= 100
        if n >= 50 and n < 100:
            i += 1
            n -= 50
        if n >= 20 and n < 50:
            i += 1
            n -= 20
        if n >= 10 and n < 20:
            i += 1
            n -= 10
    return i
