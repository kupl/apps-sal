(X, d) = map(int, input().split())
a = list()
cur = 1
for i in range(32):
    if X & 1 << i:
        for j in range(i):
            a.append(cur)
        cur = cur + d
        a.append(cur)
        cur = cur + d
print(len(a))
for i in a:
    print(i, end=' ')
