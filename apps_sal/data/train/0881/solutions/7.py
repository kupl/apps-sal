for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 c=1
 m=[]
 for i in range(n-1):
  if a[i]<=a[i+1]:
   c+=1
  else:
   m.append(c)
   c=1
 if c!=0:
  m.append(c)
 z=n 
 for i in m:
  z+=i*(i-1)//2
 print(z) 
