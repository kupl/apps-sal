n, l, r, Ql, Qr = map(int, input().split())
s, v = [0] * (n + 1), 2 * 10 ** 9
for i, wi in enumerate(map(int, input().split())):
    s[i + 1] = s[i] + wi
for lc in range(0, n + 1):
    rc = n - lc
    c = s[lc] * l + (s[n] - s[lc]) * r
    if lc > rc + 1:
        c += (lc - rc - 1) * Ql
    elif rc > lc + 1:
        c += (rc - lc - 1) * Qr
    v = min(v, c)
print(v)
