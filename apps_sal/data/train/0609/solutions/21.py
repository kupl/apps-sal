t=int(input())
for each in range(t):
 n,k=map(int,input().split())
 q=list(map(int,input().split()))
 i=0
 while True:
  if i<n:
   if i==0:
    if q[i]<k:
     print(i+1)
     break
    r=q[i]-k
    i+=1
   else:
    if (r+q[i])<k:
     print(i+1)
     break
    r=(r+q[i])-k
    i=i+1 
  else:
   print(i+(r//k)+1)
   break
