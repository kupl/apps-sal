def seven(m):
    i = 0
    while m > 99:
        i += 1
        m = m//10-2*(m%10)
    return (m,i)
