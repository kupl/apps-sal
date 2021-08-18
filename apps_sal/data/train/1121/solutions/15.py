t = int(input())
for j in range(t):
    s = input()
    h = int(s[:2])
    if h > 11:
        h -= 12
    m = int(s[3:])
    ah = h * 30 + m / 2
    am = (m // 5) * 30
    ans = abs(am - ah)
    if ans <= 180:
        if int(ans) == ans:
            print(int(ans), 'degree')
        else:
            print(ans, 'degree')
    else:
        if int(ans) == ans:
            print(360 - int(ans), 'degree')
        else:
            print(360 - ans, 'degree')
