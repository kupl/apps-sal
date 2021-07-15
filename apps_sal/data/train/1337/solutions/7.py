
from math import gcd
n_case=int(input())
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//gcd(lcm, a[i])
  return lcm

for _ in range(n_case):
    n=int(input())
    lt=list(set(map(int,input().split())))
    r=int(input())
    
    lcm=LCMofArray(lt)
    lcm+=r
    print(lcm)


