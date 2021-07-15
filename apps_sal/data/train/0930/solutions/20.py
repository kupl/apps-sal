for _ in range(int(input())):
 n=int(input())
 l=[[0 for i in range(n)] for j in range(n)]
 #print(l)
 c=1
 for i in range(n):
  for j in range(i+1):
   l[j][i-j]=c
   c+=1
 for i in range(1,n):
  for j in range(n-i):
   l[i+j][n-j-1]=c
   c+=1
 for i in range(n):
  for j in range(n):
   print(l[i][j],end=" ")
  print()
