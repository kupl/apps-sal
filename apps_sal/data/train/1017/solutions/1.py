for i in range(int(input())):
 n=[int(x) for x in input().split()]
 t=n[-1]
 n=n[:-1]
 a=0
 for i in n:
  a+=i*t
 if a>120:
  print('Yes')
 else:
  print('No')
