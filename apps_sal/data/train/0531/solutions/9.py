n=int(input())
ans=2

a=[]
for i in range(n):
 a.append(list(map(int,input().split())))
if(n==1):
 print(1)
 return
vector=a[0][0]
for i in range(1,n-1):
 if(a[i][0]-a[i][1]>vector):
  ans+=1
  vector=a[i][0]

 else:
  if(a[i][0]+a[i][1]<a[i+1][0]):
   ans+=1
   vector=a[i][0]+a[i][1]
  else:
   vector=a[i][0]
 

  
 
print(ans)

 

