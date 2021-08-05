# CLown1331 -_-
n = int(input())
ar = list(map(int, input().split()))
r = []
l = []
day = 0
for i in ar:
    day += 1
    day = min(i, day)
    l.append(day)
day = 0
for i in reversed(ar):
    day += 1
    day = min(i, day)
    r.append(day)
ans = 0
x = 0
rh = list(reversed(r))
while x < n:
    ans = max(ans, min(rh[x], l[x]))
    x += 1
print(ans)
