def two_lane(n,k,d,l,x):
 flag=0
 z=-(10**10)
 for i in range(n-1):
  if(l[i]!=l[i+1]):
   z=max(x[i]+1,z+d)
   if(z>=x[i+1]):
    return(x[i+1])
    flag=1
    break
 return k
t=int(input())
while(t):
 t-=1
 n,k,d=list(map(int,input().split()))
 x=list(map(int,input().split()))
 l=list(map(int,input().split()))
 print(two_lane(n,k,d,l,x))

