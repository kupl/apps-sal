for _ in range(int(input())):
 a,b=map(int,input().split())
 if(b==0):
  print('{} {}'.format(0,a))
 else:
  print('{} {}'.format(a//b,a%b))
