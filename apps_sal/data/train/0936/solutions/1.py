for _ in range(int(input())):
 n=int(input())
 a=[]
 l=0
 for i in range(n):
  a.append(list(map(int,input().split())))
 for i in range(n-1,0,-1):
  r=a[i][i-1]+1
  if a[i][i]!=r:
   l+=1
   n=i+1
   for j in range(n):
    for k in range(j,n):
     a[j][k],a[k][j]=a[k][j],a[j][k]
    
 print(l)
 

