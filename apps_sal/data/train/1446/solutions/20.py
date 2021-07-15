for _ in range(int(input())):
 n=int(input())
 if(n==1):
  print(2)
 else:
  arr=[]

  i=0
  while(True):
   if(2**i<=n):
    arr.append(2**i)
    i+=1
   else:
    break

  flg=0
  for i in arr:
   if(i^(i-1)==n):
    flg=1
    print(i-1)
    break

  if(not flg):
   print(-1)

