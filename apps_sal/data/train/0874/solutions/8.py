for _ in range(int(input())):
    (n, m, s) = (int(i) for i in input().split())
    li = list((int(i) for i in input().split()))
    c = 0
    d = m
    for i in li:
        if i <= s:
            c += 1
            d -= 1
    if m <= c:
        print(m)
    else:
        for i in li:
            if d < 2:
                break
            if i > s and i <= 2 * s:
                c += 1
                d -= 2
        print(c)
