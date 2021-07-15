m = int(input())
s = input()
n = len(s)
t = []
u = [1] * n
d = 'a'
i = 0
while i <= n - m:
    k = i
    for j in range(m):
        if s[i + j] <= s[k]: k = i + j
    t += [s[k]]
    d = max(d, s[k])
    u[k] = 0
    i = k + 1
t += [q for q, v in zip(s, u) if q < d and v]
print(''.join(sorted(t)))
