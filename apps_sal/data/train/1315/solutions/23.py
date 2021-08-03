from collections import Counter
l = []
for _ in range(int(input())):
    s = list(map(int, input().split()))
    s = sorted(s)
    l.append(tuple(s))

c = Counter(l)
t = 0
for v in list(c.values()):
    if v == 1:
        t += 1
print(t)
