t = eval(input())

for i in range(t):
 n=eval(input())
 a = list(map(int, input().split()))
 a.sort()
 
 cnt=1
 for ind,x in enumerate(a):
  cnt*=(x-ind) 
  if x-ind<=0:
   cnt=0
   break
 print(cnt%(10**9+7)) 

