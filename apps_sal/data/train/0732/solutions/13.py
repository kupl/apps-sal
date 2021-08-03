for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ra = [0] * n
    x = 0
    for i in range(n):
        ra[i] = x + a[i]
        x = ra[i]
    b = list(map(int, input().split()))
    rb = [0] * n
    y = 0
    for i in range(n):
        rb[i] = y + b[i]
        y = rb[i]
    c = f = 0
    if ra[0] == rb[0]:
        c = a[0]
    for i in range(1, n):
        if ra[i - 1] == rb[i - 1] and a[i] == b[i]:
            c += a[i]
    print(c)
