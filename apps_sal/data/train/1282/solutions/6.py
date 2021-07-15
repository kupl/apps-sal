mod = 10**9+7
t = int(input())
while(t>0):
 l, r = map(int, input().split())
 ans = 0
 for i in range(63):
  if(l&(1<<i)):
   x =(1<<i) - (l&((1<<i)-1))
   x = min(x, (r-l+1))
   ans += x*(1<<i)
 print(ans%mod)
 
 
 
 t = t-1
