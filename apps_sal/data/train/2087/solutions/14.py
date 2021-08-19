(n, l, r, ql, qr) = map(int, input().split())
w = list(map(int, input().split()))
s = [0, *w]
for i in range(1, n + 1):
    s[i] += s[i - 1]
c_min = s[n] * r + (n - 1) * qr
for i in range(1, n + 1):
    cc = l * s[i] + (s[n] - s[i]) * r
    if 2 * i < n:
        cc += (n - 2 * i - 1) * qr
    elif 2 * i > n:
        cc += (i - (n - i) - 1) * ql
    c_min = min(c_min, cc)
print(c_min)
