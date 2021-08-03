t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    a.sort()
    for i in range(0, n // 2):
        c += abs(a[i] - a[n - 1 - i])
    print(c)
