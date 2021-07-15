for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 m=int(input())
 b=list(map(int,input().split()))
 x=[]
 for i in range(len(b)):
  if b[i] in a :
   x.append(a.index(b[i])) 
 c=0
 for i in range(len(x)-1):
  if x[i]<x[i+1]:
   c+=1
 if c==m-1:
  print("Yes")
 else:
  print("No")
