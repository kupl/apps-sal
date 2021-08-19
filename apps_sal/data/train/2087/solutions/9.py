(n, l, r, ql, qr) = list(map(int, input().split()))
w = list(map(int, input().split()))
prefix = [0]
suffix = [sum(w)]
for i in range(n):
    prefix.append(prefix[i] + w[i])
    suffix.append(suffix[i] - w[i])
m = 10000000000.0
for i in range(n + 1):
    res = l * prefix[i] + r * suffix[i]
    if i > n - i:
        res += (2 * i - n - 1) * ql
    if i < n - i:
        res += (n - 2 * i - 1) * qr
    m = min(m, res)
print(m)
