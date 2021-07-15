from math import gcd


def LCM(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//gcd(lcm, a[i])
  return lcm



t = int(input())
while t>0:
    n = int(input())
    lst = list(map(int,input().split()))
    r = int(input())

    res = LCM(lst)

    print(res + r)

    t-=1
