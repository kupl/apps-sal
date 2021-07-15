# cook your dish here
for _ in range(int(input())):
 n,v1,v2=list(map(int,input().split()))
 t1=(n/v1)
 t2=((2**0.5)*n/v2)
 if t1>t2:
  print('Elevator')
 else:
  print('Stairs')
