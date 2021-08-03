def jump(h, m):
    diff = abs(m - h) * 30
    if m * 5 % 2 == 0:
        ahead = m * 5 // 2
    else:
        ahead = m * 5 / 2
    if h >= m:
        diff += ahead
    else:
        diff -= ahead
    if (h == 12 or h == 0) and m == 0:
        print(0, "degree")
    else:
        if diff <= 180:
            print(diff, "degree")
        else:
            print(360 - diff, "degree")


t = int(input())
for g in range(t):
    # n=int(input())
    a = input()
    h = int(a[:2])
    if h > 12:
        h -= 12
    elif h == 0:
        h = 12
    m = int(a[3:]) // 5
    jump(h, m)
