import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
yp=lambda:print('Yes')
np=lambda:print('No')

n,a,b=lp()
x=lp()
ans=0
for i in range(n-1):
  ans+=min(b,a*(x[i+1]-x[i]))
print(ans)
