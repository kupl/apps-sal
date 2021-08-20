t = int(input())
for i in range(t):
    (h, m) = list(map(int, input().split(':')))
    if h >= 12:
        h -= 12
    hm = m / 2
    a = m // 2
    mm = m // 5
    if h < mm:
        ang = abs(mm - h) * 30
        ang -= hm
        if hm == a:
            print(int(min(ang, 360 - ang)), 'degree')
        else:
            print(min(ang, 360 - ang), 'degree')
    else:
        ang = abs(h - mm) * 30
        ang += hm
        if hm == a:
            print(int(min(ang, 360 - ang)), 'degree')
        else:
            print(min(ang, 360 - ang), 'degree')
