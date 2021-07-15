t=int(input())
while t!=0:
 n=int(input())
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 alice=sum(a)-max(a)
 bob=sum(b)-max(b)
 if alice<bob:
  print('Alice')
 elif bob<alice:
  print('Bob')
 else:
  print('Draw')
 t-=1
