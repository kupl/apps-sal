# cook your dish here
for _ in range(int(input())):
 n= int(input())
 l=list(map(int,input().split()))
 N=(n)*(n+1)//2
 d=set()
 if n>60:
  print('NO')
 else:
  for i in range(n):
   ans=0
   for j in range(i,n):
    ans=l[j]|ans 
    d.add(ans)
  if len(d)==N:
   print('YES')
  else:
   print('NO')
