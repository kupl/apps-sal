# cook your dish here
import sys

mod = 998244353

input = sys.stdin.readline

t = int(input())
for _ in range(t):
 n, m = list(map(int, input().split()))
 arr1 = [int(j) for j in input().split()]
 arr2 = [int(j) for j in input().split()]

 a = sum(arr1)
 b = sum(arr2)

 q = int(input())
 for i in range(q):
  s = input().split()
  if len(s) == 1:
   print(a*b % mod)
  else:
   num, l, r, x = list(map(int, s))
   if num == 1:
    a += (r-l+1)*x
    a %= mod
   else:
    b += (r-l+1)*x
    b %= mod

