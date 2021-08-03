from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

res = 0
cur = 0
for i in sorted(c.keys()):
    d = min(c[i], cur)
    cur -= d
    res += d
    cur += c[i]

print(res)
