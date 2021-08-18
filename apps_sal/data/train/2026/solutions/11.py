def f(): return list(map(int, input().split()))


n, d = f()

a = [0] + f() + [0]

p = [f() for i in range(n)]

r = list(range(n))

s = [[d * (abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])) - a[j] * (i != j) for j in r] for i in r]

for k in r:
    s = [[min(s[i][j], s[i][k] + s[k][j]) for i in r] for j in r]

print(s[-1][0])
