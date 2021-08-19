# cook your dish here
t = int(input())
while t > 0:
    n, m, k = map(int, input().split())
    tot = 0
    l = list(map(int, input().split()))
    for i in range(0, k):
        a = l[i]
        x = (a - 1) // m + 1
        y = (a - 1) % m + 1
        tot = tot + (x * y) * (n - x + 1) * (m - y + 1)
    print("{0:.10f}".format(tot / (m * (m + 1) * n * (n + 1) // 4)))
    t = t - 1
