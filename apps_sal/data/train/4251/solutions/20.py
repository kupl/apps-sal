def difference_of_squares(n):
    if 1 <= n <= 100:
        lst = []
        for i in range(1, n + 1):
            lst.append(i)
            s = sum(lst)**2
        l = []
        for i in range(1, n + 1):
            l.append(i**2)
            t = sum(l)
    return s - t
