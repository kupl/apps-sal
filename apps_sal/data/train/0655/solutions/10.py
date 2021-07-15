# cook your dish here
for i in range(int(input())):
 n,k,v = map(int,input().split())
 l = list(map(int,input().split()))
 a = v*(k+n)
 if sum(l)>=a:
  print(-1)
 else:
  if (a-sum(l))%k!=0:
   print(-1)
  else:
   print((a-sum(l))//k)
