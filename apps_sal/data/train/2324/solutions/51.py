from collections import *
n=int(input())
ab=[[]for i in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    ab[x-1].append(y-1)
    ab[y-1].append(x-1)
s=[float("inf")]*n
f=[float("inf")]*n
q=deque()
q.append((0,0))
while q:
    a,b=q.popleft()
    if f[a]==float("inf"):
        f[a]=b
        for j in ab[a]:
            if f[j]==float("inf"):
                q.append((j,b+1))
                
d=deque()
d.append((n-1,0))
while d:
    a,b=d.popleft()
    if s[a]==float("inf"):
        s[a]=b
        for j in ab[a]:
            if s[j]==float("inf"):
                d.append((j,b+1))
sa,fa=0,0

for i in range(n):
    if s[i]>=f[i]:
        fa+=1
    else:
        sa+=1
if fa>sa:
    print("Fennec")
else:
    print("Snuke")
