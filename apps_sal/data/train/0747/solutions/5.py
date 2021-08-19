for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    b = []
    a = []
    x = 0
    l.sort()
    for i in range(n):
        if x < l[i]:
            x = l[i]
            a.append(l[i])
            l[i] = 0
            continue
        b.append(l[i])
    (x, f) = (0, 0)
    for i in b:
        if x == i:
            f = 1
        x = i
    b.sort(reverse=True)
    if len(b) == 0:
        print('YES')
        print(*a)
    elif f == 1 or a[-1] == b[0]:
        print('NO')
    else:
        print('YES')
        print(*a + b)
