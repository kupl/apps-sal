t = int(input())
for i in range(t):
    (x, y) = (0, 0)
    (n, m) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if max(l) > m:
        print(-1)
    else:
        for i in range(len(l)):
            y += l[i]
            if y > m:
                y = l[i]
                x += 1
        if y > 0:
            x += 1
        print(x)
