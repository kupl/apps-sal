t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    lmin = []
    lmax = []
    for i in range(n):
        num = l[i]
        l[i] += num % 3
    if n % 2 == 0:
        for i in range(n - 1):
            (l[i], l[i + 1]) = (l[i + 1], l[i])
    else:
        for i in range(n - 2):
            (l[i], l[i + 1]) = (l[i + 1], l[i])
    for i in range(int(n / 2)):
        (l[i], l[n - 1 - i]) = (l[n - 1 - i], l[i])
    for i in range(len(l)):
        if l[i] < m:
            lmin.append(l[i])
        elif l[i] > m:
            lmax.append(l[i])
    if len(lmin) == 0:
        a = -1
    else:
        a = max(lmin)
    if len(lmax) == 0:
        b = -1
    else:
        b = min(lmax)
    print(a, b)
