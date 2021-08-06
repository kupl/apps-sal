s, t = input(), input()
n, m = len(t), len(s) + 1

d = 1000000007
g = [1] * m

f = k = 0
for i in range(1, m):
    if s[i - n:i] == t:
        k = i
    if k:
        f = (f + g[k - n]) % d
    g[i] += (g[i - 1] + f) % d

print(f)
