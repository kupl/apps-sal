def cycle(n) :
    if n%2 == 0 or n%5 == 0:
        return -1
    c = len(str(n))
    m = 10**c % n
    while m != 1:
        c += 1
        m = (m*10) % n
    return c

