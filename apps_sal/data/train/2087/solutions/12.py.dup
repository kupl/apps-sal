n, l, r, ql, qr = map(int, input().split())
w = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    w[i] += w[i - 1]
s = w[n]
print(min(l * w[i] + r * (s - w[i]) + ql * max(0, 2 * i - n - 1) + qr * max(0, n - 2 * i - 1) for i in range(n + 1)))
