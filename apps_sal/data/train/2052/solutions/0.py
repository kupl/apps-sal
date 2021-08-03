n, m = list(map(int, input().split()))
used = [1] * 2 * n
for i in range(m):
    x, y = list(map(int, input().split()))
    used[x - 1] = used[n + y - 1] = 0

if n % 2 and used[n // 2]:
    used[n // 2 + n] = 0
res = sum(used)
for i in [0, n - 1, n, 2 * n - 1]:
    res -= used[i]
print(res)
