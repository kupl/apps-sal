n = int(input())
d = {}
s = 0
for i in range(n):
    t = list(map(int, input().split()))
    t.sort()
    t = tuple(t)
    if t in d:
        d[t] = d[t] + 1
        s = s - 1
    else:
        d[t] = 1
        s = s + 1
print(s)
