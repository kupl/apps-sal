for _ in range(int(input())):
    (n, l, r) = map(int, input().split())
    mi = n - l + 1
    p = 1
    for x in range(n - mi):
        mi = mi + 2 ** p
        p += 1
    p1 = 0
    t = 0
    for y in range(r - 1):
        p1 += 1
        t = t + 2 ** p1
    t = t + (n - r) * 2 ** p1
    print(mi, t + 1)
