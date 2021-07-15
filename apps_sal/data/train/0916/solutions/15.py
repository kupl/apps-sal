from math import gcd
def lcm(a,b):
  return int((a*b/gcd(a,b)))

t=int(input())
while (t!=0):
  n,m=list(map(int,input().split()))
  ans=lcm(n,m)
  print(ans)
  t=t-1

