# cook your dish here
t=int(input())
for t1 in range(t):
 n=int(input())
 l=[int(x) for x in input().split()]
 prod=1
 for i in l:
  prod=prod*i
 if(prod%2==1):
  print('YES')
 else:
  print('NO')
