for q in range(int(input())):
 n,k=list(map(int,input().split()))
 test=[]
 z=[]
 f=0
 for i in range(n):
  l=[int(i) for i in input().split()]
  l=l[1:]
  z.append(l)
 c=[0]*(k+1)
 for i in range(n):
  for j in z[i]:
   c[j]+=1
 for i in range(1,k+1):
  if c[i]==0:
   print("sad")
   f=1
   break
 if f==1:
  continue
 for i in range(n):
  cnt=0
  for j in z[i]:
   if c[j]!=1:
    cnt+=1
  if cnt==len(z[i]):
   print("some")
   break
 else:
  print("all")
   
    
   

