def multiples(m, n):
    arr = []
    s = 1
    k = 0
    while m > 0:
        k = n * s
        s += 1
        m -= 1
        arr.append(k)
    return arr
