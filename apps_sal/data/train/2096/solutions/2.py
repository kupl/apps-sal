n = int(input())

a = input().split()
a = [(int(a[i]), i) for i in range(n)]
a.sort()

start = 0
used = set()

b = []

while start < n:
    t = []
    cur = start
    first = True

    while cur != start or first:
        first = False
        t.append(cur + 1)
        used.add(cur)
        cur = a[cur][1]

    b.append(t)
    while start in used:
        start += 1

print(len(b))

for t in b:
    print(len(t), end=' ')
    print(*t)
