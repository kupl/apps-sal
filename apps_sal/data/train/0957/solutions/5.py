t = int(input())
for rep in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    l = []
    if n > 2:
        for i in range(1, n - 1):
            l.append(min(x[i] - x[i - 1], x[i + 1] - x[i]))
        l.append(x[1] - x[0])
        l.append(x[n - 1] - x[n - 2])
    else:
        l.append(x[1] - x[0])
    print(max(l))
