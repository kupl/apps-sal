r,c,n=map(int,input().split())
a=[[0 for i in range(c)] for j in range(r)]

for i in range(n):
    c1,d1=map(int,input().split())
    a[c1][d1]=1 
    

a2=[[0 for i in range(r)] for j in range(c)]

#print(a2)

for i in range(c):
    for j in range(r):
        a2[i][j]=a[j][i]
        
        
#print(a,a2)
c2=[0 for i in range(r)]
d2=[0 for j in range(c)]

for i in range(r):
    c2[i]=sum(a[i])
    
for i in range(c):
    d2[i]=sum(a2[i])
#print(c,d)
    
ans=0

for i in range(r):
    for j in range(c):
        if a[i][j]==1:
            ans=max(ans,c2[i]+d2[j]-1)
        else:
            ans=max(ans,c2[i]+d2[j])
        
print(ans)
