t = int(input())
while t > 0:
    a = int(input())
    ta = 0
    gi = 0
    c = 1
    i = 0
    d = 0
    ma = 0
    while True:
        ta += a
        gi += c
        c *= 2
        i += 1
        if ta - gi > ma:
            ma = ta - gi
            d = i
        if ta - gi < 0:
            i -= 1
            break
    print(i, d)
    t -= 1
