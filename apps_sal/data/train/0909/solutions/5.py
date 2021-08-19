for _ in range(int(input())):
    n = int(input())
    b = sorted(list(map(int, input().split())))
    g = sorted(list(map(int, input().split())))
    (b1, g1) = ([], [])
    (B, G) = (0, 0)
    count = 0
    for i in range(n):
        b1.append(b[i])
        b1.append(g[i])
        g1.append(g[i])
        g1.append(b[i])
    for i in range(n * 2 - 1):
        if b1[i] <= b1[i + 1]:
            B += 1
        if g1[i] <= g1[i + 1]:
            G += 1
    if B == n * 2 - 1 or G == n * 2 - 1:
        print('YES')
    else:
        print('NO')
