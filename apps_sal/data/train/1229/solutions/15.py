for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = []
    t = []
    for i in range(n):
        if i % 2 == 0:
            m.append(a[i])
        else:
            t.append(a[i])
    m.sort(reverse=True)
    t.sort()
    mi = min(len(m), len(t))
    x1 = 0
    x2 = 0
    while k != 0 and x1 < len(m) and (x2 < len(m)):
        if m[x1] > t[x2]:
            (m[x1], t[x2]) = (t[x2], m[x1])
            x1 += 1
            x2 += 1
        else:
            break
        k -= 1
    if sum(t) > sum(m):
        print('YES')
    else:
        print('NO')
