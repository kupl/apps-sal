def seven(m):
    i = 0
    while m > 99:
        x10 = m//10
        y = m % 10
        m = x10 -2*y
        i += 1
    return (m,i)
