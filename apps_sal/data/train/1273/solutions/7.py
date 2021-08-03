t = int(input())
for i in range(t):
    nm = str(input()).split()
    n = int(nm[0])
    m = int(nm[1])
    up = n
    dn = -1
    l = m
    r = -1
    for j in range(n):
        inp = str(input())
        if '*' in inp:
            p1 = inp.find('*')
            p2t = (inp[::-1]).find('*')
            p2 = m - p2t - 1
            if j < up:
                up = j
            if j > dn:
                dn = j
            if p1 < l:
                l = p1
            if p2 > r:
                r = p2
    if dn == -1:
        print(0)
    else:
        r1 = (dn - up) / 2 + (dn - up) % 2 + 1
        r2 = (r - l) / 2 + (r - l) % 2 + 1
        print(max(r1, r2))
