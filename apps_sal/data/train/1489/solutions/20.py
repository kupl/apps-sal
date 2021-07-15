n,k=input().split()
k=int(k)
l=len(n)
ans=""
for i in range(l):
    if k==0:
        break
    if n[i]!='9':
        ans+='9'
        k-=1
    else:
        ans+=n[i]
if len(ans)==l:
    print(ans)
else:
    for j in range(len(ans),l):
        ans+=n[j]
    print(ans)
