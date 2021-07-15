import sys

s=list(map(int,list(input())))
n=len(s)
if s[0]==0 or s[-1]==1:
    print(-1)
    return
for i in range(n//2):
    if s[i]==s[n-2-i]:
        continue
    else:
        print(-1)
        return
ans=[[1,2]]
last_edge=2
for i in range(3,n+1):
    ans.append([last_edge,i])
    if s[i-2]==1:
        last_edge=i
for u in ans:
    print(*u)
