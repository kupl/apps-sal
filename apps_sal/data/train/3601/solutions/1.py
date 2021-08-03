def find_nb(m):
    n = s = 0
    while True:
        n += 1
        s += n
        k = s * s
        if k == m:
            return n
        elif k > m:
            return -1
