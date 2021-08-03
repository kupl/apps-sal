n = int(input())
f = [[a, 1] for a in map(int, input().split())]
def dot(p, q): return sorted(p + q)[-2:]


for d in range(n):
    for U in range(1 << n):
        if not U >> d & 1:
            f[U | 1 << d] = dot(f[U | 1 << d], f[U])

res = 0
for i in range(1, 1 << n):
    res = max(res, sum(f[i]))
    print(res)
