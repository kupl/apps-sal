l = [1]
for i in range(1, 21):
    x = 2 ** i
    l.append(x)
for _ in range(int(input())):
    (n, a, r) = list(map(int, input().split()))
    tmi = n
    tma = n
    miv = 0
    mav = 0
    while tmi != 0:
        if a == 1:
            miv = l[0] * n
            tmi = 0
        else:
            miv = sum(l[:a])
            tmi = tmi - a
            miv = miv + tmi * l[0]
            tmi = 0
    x = l[:r]
    ll = len(x)
    while tma != 0:
        if r == 1:
            mav = l[0] * n
            tma = 0
        else:
            mav = mav + sum(l[:r])
            tma = tma - r
            mav = mav + tma * x[ll - 1]
            tma = 0
    print(min(mav, miv), max(miv, mav))
