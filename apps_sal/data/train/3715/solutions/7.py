def nth_chandos_number(n):  # :( stupid code
    a, i, j, m = [], -1, 1, 5
    while len(a) < n:
        m = 5 ** j
        a.append(m)
        while j > 1 and i < 2 ** ~-j - 1:
            a.append(m + a[i])
            i += 1
        i, j = 0, j + 1
    return a[~-n]
