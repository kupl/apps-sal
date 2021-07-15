mod=int(1e9)+7
t=int(input())
while t:
 t-=1
 l, r= map(int , input().split())
 binl=bin(l)[:1:-1]
 f, cnt, ans=1, 0, 0
 for i in binl:
  if i=='1':
   ans= (ans+f*min(f-cnt, r-l+1))%mod
   cnt+=f
  f*=2
 print(ans)
