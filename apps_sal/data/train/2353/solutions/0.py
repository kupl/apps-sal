n, a = int(input()), [int(i) for i in input().split()]
b, m = a[:], dict()
b.sort()
for i in range(len(b) - 1):
    m[b[i]] = b[i + 1]
m[b[-1]] = b[0]
for i in range(len(a)):
    a[i] = m[a[i]]
if len(set(b)) == n:
    print(*a)
else:
    print(-1)

