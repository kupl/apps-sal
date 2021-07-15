for _ in range(int(input())):
 n,v1,v2=map(int,input().split())
 if (n/v1)<=((2**0.5)*n/v2):
  print('Stairs')
 else:
  print('Elevator')
