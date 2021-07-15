import math

def LCM(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

t=int(input())
for _ in range(t):
    n=int(input())
    guest=list(map(int,input().split()))
    r=int(input())
    lcm=LCM(guest)
    print(lcm+r)

