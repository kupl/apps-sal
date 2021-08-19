t = int(input())
while t > 0:
    a = input().split(':')
    a1 = int(a[0])
    a2 = int(a[1])
    b1 = a1 % 12
    if a2 % 5 != 0:
        b2 = a2 // 5 * 5 + 5
    else:
        b2 = a2
    c1 = b1 * 30
    extra = 0.5 * b2
    c1 += extra
    c1 %= 360
    d1 = b2 // 5 * 30
    d1 %= 360
    if c1 > d1:
        ans1 = c1 - d1
        ans2 = 360 - ans1
    else:
        ans1 = d1 - c1
        ans2 = 360 - ans1
    ans = min(ans1, ans2)
    if ans == int(ans):
        ans3 = int(ans)
        y = str(ans3) + ' degree'
        print(y)
    else:
        y = str(ans) + ' degree'
        print(y)
    t -= 1
