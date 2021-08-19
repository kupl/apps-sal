(s, t) = (input(), input())
(n, m) = (len(t), len(s))
d = 10 ** 9 + 7
p = [0] * (n + 1)
(i, j) = (0, 1)
while j < n:
    if t[i] == t[j]:
        j += 1
        i += 1
        p[j] = i
    elif i:
        i = p[i]
    else:
        j += 1
i = j = 0
f = [0] * (m + 1)
while j < m:
    if t[i] == s[j]:
        i += 1
        j += 1
        if i == n:
            i = p[i]
            f[j - n] = 1
    elif i:
        i = p[i]
    else:
        j += 1
s = [0] * (m + 1)
k = m
for j in range(m - 1, -1, -1):
    if f[j]:
        k = j
    if k < m:
        f[j] = (f[j + 1] + s[k + n] + m - k - n + 1) % d
        s[j] = (s[j + 1] + f[j]) % d
print(f[0])
