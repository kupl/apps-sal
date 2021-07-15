t=int(input())
for i in range(t):
 p=[int(x) for x in input().split()]
 a=p[-1]
 p=p[:-1]
 n=0
 for i in p:
  n+=i*a
 if n>120:
  print('Yes')
 else:
  print('No')
