t = int(input())
for i in range(t):
    a = []
    n = int(input())
    for i in range(n):
        x, y = [int(i) for i in input().split()]
        a.append((x, y))
    a.sort()
    # print(a)
    q = a[0][0]
    z = []
    for i in range(1, n):
        # print(a[i][0],q)
        if a[i][0] != q:
            z.append(a[i - 1][1])
            # print(a[i])
            q = a[i][0]
    z.append(a[n - 1][1])
    l = len(z)
    if l < 3:
        print(0)
    else:
        z.sort()
        print(z[l - 1] + z[l - 2] + z[l - 3])
