t = int(input())

while t != 0:
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    flag = 1

    s = list(set(a))
    for i in s:
        if a.count(i) > 2:
            flag = 0

    if flag == 0 or a.count(m) != 1:
        print("NO")
    else:
        print("YES")
        r = []
        for i in s:
            if a.count(i) > 1:
                r.append(i)

        r = sorted(r, reverse=True)
        s1 = sorted(s) + r
        print(*s1)

    t -= 1
