f = lambda: list(map(int, input().split()))
n, d = f()
r = range(n)
a = [0] + f() + [0]
p = [f() for i in r]
s = [1e9] * n
q, s[0] = 1, 0
while q:
    q = 0
    for i in r:
        for j in r:
            if i != j:
                t = s[i] + (abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])) * d - a[j]
                if t < s[j]: q, s[j] = 1, t
print(s[-1])
