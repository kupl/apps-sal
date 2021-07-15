n = int(input())
l, r = [0] * n, [0] * n
f = lambda x, y: all(x > r[j] or y < l[j] for j in range(i))

for i in range(n):
    x, d = map(int, input().split())
    y = x + d - 1

    if not f(x, y):
        k = min(r[j] for j in range(i + 1) if f(r[j] + 1, r[j] + d))
        x, y = k + 1, k + d

    l[i], r[i] = x, y
    print(x, y)
