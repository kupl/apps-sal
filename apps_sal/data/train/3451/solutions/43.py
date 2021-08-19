def triangle(a):
    q = len(a)
    if q == 1:
        return a
    b = 1
    g = 2
    r = 3
    a = a.replace('B', '1')
    a = a.replace('G', '2')
    a = a.replace('R', '3')
    v = int(a)
    count = 0
    while q != 1:
        for i in range(1, q):
            if v // 10 ** (q - i) - 10 * (v // 10 ** (q - i + 1)) == v // 10 ** (q - i - 1) - 10 * (v // 10 ** (q - i)):
                e = v // 10 ** (q - i) - 10 * (v // 10 ** (q - i + 1))
            else:
                e = 6 - (v // 10 ** (q - i) - 10 * (v // 10 ** (q - i + 1)) + v // 10 ** (q - i - 1) - 10 * (v // 10 ** (q - i)))
            count = count + e * 10 ** (q - i - 1)
        q = q - 1
        v = count
        if q == 1:
            if count == 1:
                return 'B'
            elif count == 2:
                return 'G'
            else:
                return 'R'
        count = 0
