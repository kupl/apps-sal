n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = []
for i in range(n):
    p.append((b[i], i + 1))
# print(p)
p.sort()
# print(p)
a.sort()
# print(a)
a.reverse()
# print(a)
c = [0] * (n + 1)
for i in range(n):
    # print(p[i][1],a[i])
    c[p[i][1]] = a[i]
for i in range(n):
    print(c[i + 1], end=" ")
