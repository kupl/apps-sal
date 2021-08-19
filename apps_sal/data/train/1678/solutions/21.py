(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = a.index(min(a))
y = b.index(max(b))
for i in range(m):
    print(x, i)
for i in range(n):
    if i != x:
        print(i, y)
