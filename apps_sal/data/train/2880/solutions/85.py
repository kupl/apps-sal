def seven(m):
    x = m
    i = 0
    while x >= 100:
        if x > 0:
            x = m // 10 - 2 * (m % 10)
            m = x
            i +=1
    return m, i

