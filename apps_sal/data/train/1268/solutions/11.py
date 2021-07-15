def __starting_point():
 while(True):
  n,m,x=map(int,input().split())
  if(n==0 and m==0 and x==0):
   break
  sum=0
  for i in range(n):
   sum+=(x+i*m)//n
  print(sum)
__starting_point()
