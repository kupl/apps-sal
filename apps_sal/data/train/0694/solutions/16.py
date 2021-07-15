from functools import reduce
from math import gcd
def lcm(a, b):
 return int(a*b/gcd(a,b))
def lcms(*numbers):
 return reduce(lcm, numbers)
for _ in range(int(input())):
 d = int(input())
 num = list(map(int, input().split()))
 x = lcms(*num)/24
 print(int(d//x))
 

