n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    d[a[i]] = 0

for i in range(n):
    for j in range(i, n):
        l = a[i:j + 1]
        d[min(l)] += 1

q = int(input())
for _ in range(q):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        print(0)
