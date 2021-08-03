try:
    def total(i, t):
        dec = 0
        t1 = t
        for i in range(i - 1):
            dec = (t1 * 2) / 100
            t1 = dec
        earn = t - (i * dec)
        return earn
    d, w, t = list(map(int, input().split()))
    s = list(map(int, input().split()))
    m = 0
    for i in s:
        m = m + w + total(i, t)
    if m >= 300:
        print("YES")
    else:
        print("NO")
except:
    pass
