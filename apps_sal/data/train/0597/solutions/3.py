t = int(input())
for i in range(t):
    n = int(input())
    xl = []
    hl = []
    for j in range(n):
        (x, h) = list(map(int, input().strip().split()))
        xl.append(x)
        hl.append(h)
    a = [0 for j in range(n)]
    a[0] = xl[1] - xl[0]
    for j in range(1, n - 1):
        a[j] = xl[j + 1] - xl[j - 1]
    a[n - 1] = xl[n - 1] - xl[n - 2]
    a.sort()
    hl.sort()
    sum = 0
    for j in range(n):
        sum += a[j] * hl[j]
    print(sum)
