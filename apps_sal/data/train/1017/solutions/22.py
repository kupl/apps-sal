for i in range(int(input())):
 x=list(map(int,input().split())) 
 e=x[-1] 
 del x[-1]
 res=[p*e for p in x]
 if sum(res)<=120:
  print('No') 
 else:
  print('Yes')

