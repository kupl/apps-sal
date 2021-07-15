try:
 t=int(input())
 while t>0:
  [x,y,K,N]=[int(x) for x in input().split()]
  if abs(x-y)%(2*K)==0:
   print('Yes')
  else:
   print('No')
  t-=1
except:
 pass
