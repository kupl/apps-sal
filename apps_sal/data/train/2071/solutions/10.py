from collections import defaultdict, Counter

n = int(input())

w = []
for i in range(n):
    w.append(tuple(map(int, input().split())))

dx = Counter()
dy = Counter()
for x, y in w:
    dx[x] += 1
    dy[y] += 1

count = sum((v * (v - 1) / 2) for v in list(dx.values())) + sum((v * (v - 1) / 2) for v in list(dy.values()))

dc = Counter(w)
count -= sum((c * (c - 1) / 2) for c in list(dc.values()) if c > 1)

print(int(count))
