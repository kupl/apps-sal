def seven(m):
    i = 0
    while m>99:
        m = m//10 - 2*(m%10)
        i += 1
    return (m,i)
