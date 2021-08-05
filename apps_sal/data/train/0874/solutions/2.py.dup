for _ in range(int(input())):
    n, m, s = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    x = m * s
    c = 0
    for i in l:
        if i <= s and m >= 1:
            c += 1
            m -= 1
        else:
            if i <= 2 * s and m >= 2:
                c += 1
                m -= 2
    print(c)
