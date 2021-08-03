N, T = map(int, input().split())
a = [int(i) for i in input().split()]
b = [a[0]]
m = b[0]
for i in range(1, N):
    if m > a[i]:
        m = a[i]
    b.append(m)
c = [a[i] - b[i] for i in range(N)]
print(c.count(max(c)))
