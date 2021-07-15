q=int(input())
for _ in range(q):
  n,m=list(map(int,input().split()))
  a,b=divmod(n//m,10)
  ans=0
  ans_t=0
  for i in range(1,b+1):
    ans+=(i*m)%10
  for i in range(1,10):
    ans_t+=(i*m)%10
  print(ans+ans_t*a)



