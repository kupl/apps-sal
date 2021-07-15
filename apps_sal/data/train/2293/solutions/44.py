def upd(now,x):
  if now[0]<x:
    now=[x,now[0]]
  elif now[1]<x:
    now[1]=x
  return now

def update(now,next):
  ary=now+next
  ary.sort(reverse=True)
  return ary[:2]


def main(n,a):
  dp=[[a[i],0] for i in range(2**n)]
  #dp[0][0]=a[0]
  now=a[0]
  for j in range(n):
    bit=1<<j
    for i in range(1<<n):
      if i&bit==0:
        # i|bit:iを部分集合として含む数字
        dp[i|bit]=update(dp[i],dp[i^bit])
  now=sum(dp[0])
  for k in range(1,2**n):
    now=max(now,sum(dp[k]))
    print(now)
n=int(input())
a=list(map(int,input().split()))
main(n,a)


