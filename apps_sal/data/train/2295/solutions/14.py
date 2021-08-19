n = int(input())
(a, b) = ([], [])
for i in range(n):
    (x, y) = map(int, input().split())
    a.append(x)
    b.append(y)
c = float('inf')
for i in range(n):
    if a[i] > b[i]:
        c = min(c, b[i])
print(max(0, sum(a) - c))
