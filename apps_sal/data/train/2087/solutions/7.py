n, l, r, q1, q2 = list(map(int, input().split()))
item = list(map(int, input().split()))

pre = [item[0]] + [0 for i in range(1, n)]
suf = [0 for i in range(0, n - 1)] + [item[n - 1], 0]
for i in range(1, n):
    pre[i] = pre[i - 1] + item[i]
for i in range(n - 2, -1, -1):
    suf[i] = suf[i + 1] + item[i]

ans = 1e20
for i in range(0, n):
    a, b = i + 1, n - i - 1
    c = pre[i] * l + suf[i + 1] * r + (q1 * (a - b - 1) if a > b else q2 * (b - a - 1) if b > a else 0)
    ans = min(ans, c)
ans = min(ans, suf[0] * r + q2 * (n - 1))
print(ans)
