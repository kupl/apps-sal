lim=100007
z=(10**9+7)
a=[0]*lim
a[2]=1
for i in range(3,lim):
 a[i]=a[i-1]+a[i-2]+a[i-3]
b=[0]*lim
b[1]=1
b[0]=1
for i in range(3,lim):
 b[i]=b[i-1]+b[i-2]+b[i-3]
 
for _ in range(0,int(input())):
 inp=int(input())
 print(b[inp+1]%z,a[inp+1]%z)

