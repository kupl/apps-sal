n=int(input())
a=[0] + list(map(int,input().split()))
d={}
for i in range(1,n+1):
    d[a[i]]=i
ans=0
for i in range(1,n+1):
    if a[i]!=i:
        ind1=d[a[i]]
        ind2=d[i]
        va1=a[i]
        val2=i
        a[ind1],a[ind2]=a[ind2],a[ind1]
        d[i]=i
        d[va1]=ind2
        ans+=1
        
    # print(a,ans,d)    
# print(ans)
if (3*n - ans)%2==0:
    print("Petr")
else:
    print("Um_nik")
    

