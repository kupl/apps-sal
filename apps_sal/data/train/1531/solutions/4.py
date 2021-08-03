n = int(input())
a1 = map(int, input().split())
m = int(input())
a1 = list(a1)
a1.insert(0, 0)
a1.insert(n + 1, 0)
for i in range(m):
    x, y = map(int, input().split())
    a1[x - 1] += y - 1
    a1[x + 1] += a1[x] - y
    a1[x] = 0
for i in range(1, n + 1):
    print(a1[i])
