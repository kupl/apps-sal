#CLown1331 -_-
n = int(input())
ar = list(map(int,input().split()))
r = []
l = []
day = 0
for i in ar:
    day += 1
    day = min(i,day)
    l.append(day)
day = 0
for i in reversed(ar):
    day += 1
    day = min(i,day)
    r.append(day)
ans = 0
x = 0
kk = n-1
while x < n:
    ans = max(ans,min(r[kk],l[x]))
    x += 1
    kk -= 1
print (ans)
