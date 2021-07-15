t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 o=0
 e=0
 for j in a:
  if(j%2==0):
   e+=1
  else:
   o+=1
 print(o*e) 
