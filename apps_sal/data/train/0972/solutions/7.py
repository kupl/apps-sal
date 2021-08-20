from sys import stdin, stdout
for _ in range(1):
    (n, k) = list(map(int, stdin.readline().split()))
    a = []
    ans = float('inf')
    for _ in range(n):
        a += [int(stdin.readline())]
    a.sort()
    for i in range(n - k + 1):
        ans = min(ans, abs(a[i] - a[i + k - 1]))
    print(ans)
