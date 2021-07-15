n=int(input())
a=[int(x) for x in input().split()]
t=q=int(input())
maxarr=[-1]*n
maxGlob=-1
quer=[]
while t>0:
    quer.append([int(x) for x in input().split()])
    t-=1
for i in range(q-1,-1,-1):
    k=quer[i]
    if k[0]==2:
        maxGlob=max(maxGlob,k[1])
    else:
        if maxarr[k[1]-1]==-1:
            maxarr[k[1]-1]=max(k[2],maxGlob)
 
for i in range(n):
    if maxarr[i]==-1:
        maxarr[i]=(max(maxGlob,a[i]))
    
print(*maxarr)
