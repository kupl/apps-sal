t=int(input())
for _ in range(t):
 x,y=list(map(int,input().split()))
 if((x*y)%2==0):
  print('YES')
 else:
  print('NO')


