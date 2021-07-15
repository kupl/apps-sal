for i in range(int(input())):
 n,m=map(int,input().split())
 k=list(map(int,input().split()))
 c=0
 for i in k:
  if i>=m:
   c=1
   break
 if c==1:
  print('YES')
 else:
  print('NO')
