import math
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 x=sum(a)-max(a)
 y=sum(b)-max(b)
 if x<y:
  print('Alice')
 elif x>y:
  print('Bob')
 else:
  print('Draw')

