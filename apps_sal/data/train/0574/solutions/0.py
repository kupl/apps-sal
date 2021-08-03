for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    l = []
    for i in range(n):
        if (a[i] < 0):
            e = i
            ss = sum(a[s:e])
            l.append((ss, e - s, n - s))
            s = i + 1
    e = n
    ss = sum(a[s:e])
    l.append((ss, e - s, n - s))
    x = max(l)
    s = n - x[2]
    e = x[1] + s
    for i in range(s, e):
        print(a[i], end=' ')
    print("")
