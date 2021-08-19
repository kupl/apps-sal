t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    g = 1
    for j in range(1, n):
        if j - 5 < 0:
            mi = min(a[0:j])
            if mi > a[j]:
                g = g + 1
        else:
            mi = min(a[j - 5:j])
            if mi > a[j]:
                g = g + 1
    print(g)
