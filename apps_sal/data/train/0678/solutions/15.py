t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    z = 1
    k = 0
    cnt = 0
    s = 1
    b = a.copy()
    g = 1
    k = 0
    while g < n:
        b[g] = b[g - 1] + b[g]
        g = g + 1
    while z < n:
        cnt = cnt + 1
        s = s + b[z - 1]
        k = k + 1
        if s >= n:
            break
        z = s
        if z >= n:
            break
        k = 0
    print(cnt)
    t = t - 1
