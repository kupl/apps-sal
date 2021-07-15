t=int(input())
for i in range(0,t):
 n,k=map(int,input().split())
 a1,*a=map(int,input().split())
 a.insert(0,a1)
 b=[]
 j=0
 while j<n:
  if a[j]%k==0:
   b.append(1)
  else:
   b.append(0)
  j+=1
 l=0
 while l<n:
  print(b[l],end="")
  l+=1
 print("")
