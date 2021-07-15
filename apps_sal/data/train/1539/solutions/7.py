n=int(input())
for i in range(0,n):
 s=0
 r1=input().strip()
 r2=input().strip()
 for i in r2:
  if i in r1:
   s+=1
 print(s)
