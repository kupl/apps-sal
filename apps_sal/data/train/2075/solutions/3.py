from collections import defaultdict
n, k, p = 0, 0, defaultdict(int)
input()
for i in map(int, input().split()):
    p[i] += 1
for i in map(int, input().split()):
    p[i] -= 1
r = sorted(list(p.keys()), reverse=True)
for i in r:
    n += p[i]
    if n > 0:
        break
print('YES' if n > 0 else 'NO')
