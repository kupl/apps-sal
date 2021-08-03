n = int(input())
a = []
size = (2 * n) - 1
b = [n] * size
size -= 2
curr = n - 1
a.append(b)
for i in range(n - 1):
    c = b.copy()
    c[i + 1:i + 1 + size] = [curr] * size
    a.append(c)
    b = c.copy()
    curr -= 1
    size -= 2
for i in range(len(a)):
    print(*a[i])
for i in range(len(a) - 2, -1, -1):
    print(*a[i])
