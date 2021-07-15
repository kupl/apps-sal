t=int(input())
for tc in range(t):
 n,m=map(int,input().split())
 s=n*m
 x=[]
 y=[]
 z=[]
 a=[]
 print(n*m,end=" ")
 for i in range(1,n+1):
  for j in range(1,m+1):
   x.append([i,j])
 for j in range(1,m+1):
  for i in range(1,n+1):
   y.append([i,j])
 for k in range(1,m*n):
  a=[]
  z=[]
  for i in range(0,n*m,k+1):
   z.append(x[i])
  for j in range(0,n*m,k+1):
   z.append(y[j]) 
  for i in z:
   if i not in a:
    a.append(i) 
  print(len(a),end=" ")
 print()

