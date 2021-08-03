def thirt(n):
    w = [1, 10, 9, 12, 3, 4]
    while True:
        r = n
        q = -1
        c = 0
        j = 0
        while (q != 0):
            q = int(r / 10)
            c += (r % 10) * w[j % 6]
            r = q
            j += 1
        if (c == n):
            return c
        n = c
