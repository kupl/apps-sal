for _ in range(int(input())):
    s = input()
    h = int(s[:2])
    m = int(s[3:])
    if h >= 12:
        h -= 12
    m1 = m / 2
    if m % 2 == 0:
        m1 = int(m1)
    hd = h * 30 + m1
    md = m * 6
    ans = abs(hd - md)
    if ans > 180:
        ans = 360 - ans
    print(str(ans) + ' degree')
