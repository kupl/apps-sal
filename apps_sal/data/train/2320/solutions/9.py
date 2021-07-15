m = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = sorted((bi, i) for i, bi in enumerate(map(int, input().split())))
v = [None] * m
for i in range(m):
    v[b[i][1]] = str(a[i])
print(' '.join(v))
