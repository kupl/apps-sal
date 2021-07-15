# cook your dish here
from functools import reduce
from math import gcd

for _ in range(int(input())):
 n = int(input())
 a = [int(i) for i in input().split()]
 arr = []
 val = 0
 for i in a:
  arr.append(i-val)
  val = i
  
 arr[0] = 360 - (val-arr[0])
 arr.append(360)
 q = reduce(gcd, arr)
 needed = 360/q
 print(int(needed - n))
