# cook your dish here
t=int(input())
for _ in range(t):
 flag=0
 n,m=[int(x) for x in input().split()]
 A=[None]*n
 for i in range(n):
  sint=input()
  inp=[None]*m
  for j in range(m):
   inp[j]=int(sint[j])
  A[i]=inp
 
 # print("A=",A)
 B=[[-1 for j in range(m)]for i in range(n)]

 
 row={}
 column={}
 for i in range(n):
  row[i]=0
 for j in range(m):
  column[j]=0
 # print("B=",B)  
 for i in range(n):
  for j in range(m):
   if(A[i][j]==1):
    flag=1
    row[i]=1
    column[j]=1
    B[i][j]=0
    
 if(flag==0):
  pass
 else:
  for i in range(n):
   for j in range(m):
    if(A[i][j]==0):
     if(row[i]==1 or column[j]==1):
      B[i][j]=1
     else:
      B[i][j]=2
   
    
 for i in range(n):
  print(*B[i])
 

