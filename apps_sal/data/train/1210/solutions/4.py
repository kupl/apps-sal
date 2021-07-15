for zz in range(int(input())):
 n,x = list(map(int,input().split()))
 z = list(str(input())) 
 c1 = z[0]
 c2 = z[2]
 if c1 == 'L':
  ans1 = x
 else:
  ans1 = (n+1)-x
 if ans1 % 2 == 1:
  ans2 = c2
 else:
  if c2 == 'H':
   ans2 = 'E'
  else:
   ans2 = 'H'
 print(ans1,ans2)

