s, t = input(), input()
n, m = len(t), len(s) + 1
h = t + ' ' + s

d = 1000000007
s = [1] * m

f = i = k = 0
p = [-1] + [0] * len(h)
for j in range(1, n + m):
    while i + 1 and h[i] != h[j]: i = p[i]
    i += 1
    p[j + 1] = i

    if j > n:
        j -= n
        if i == n: k = j
        if k: f = (f + s[k - n]) % d
        s[j] += (s[j - 1] + f) % d

print(f)
