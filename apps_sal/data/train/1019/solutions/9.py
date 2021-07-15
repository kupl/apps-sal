# cook your dish here
for _ in range(int(input())):
 n=int(input())
 x=list(map(int,input().split()))
 if(n%2==0):
  print('no')
 else:
  t=1
  pulkit=0
  for i in range(0,n//2+1):
   if(x[i]==x[n-i-1]==t):
    t=t+1
   else:
    pulkit=1
    break
  if(pulkit==0):
   print('yes')
  else:
   print('no')
