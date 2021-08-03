tc = int(input())
for case in range(tc):
    m, r = list(map(int, input().split()))
    n = m**(r - 1)
    a = [i**n for i in range(1, 2 * n + 1)]
    tmp = 2 * n - 1
    for i in range(n):
        for j in range(tmp - i):
            a[j] = a[j + 1] - a[j]
    print((a[n - 1] / m) % 1000000007)
