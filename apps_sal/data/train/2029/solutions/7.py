import sys
n=int(input())
if(n%2==0):
    print("NO")
    return
ans=[]
used=[]
def add(x):
    if(used[x]==0 and x<=2*n):
        used[x]=1
        ans.append(x);

for i in range(2*n+7):
    used.append(0)

ans.append(1)
used[1]=1
p=int(4)
while True:
    if(used[p]==1):
        break
    add(p)
    p+=1
    add(p)
    p+=3
    if(p>2*n):
        p=2
print("YES")
for i in range(2*n):
    print(ans[i],end=' ')
