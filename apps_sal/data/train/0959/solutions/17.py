# cook your dish here
from fractions import Fraction
for i in range(int(input())):
 N=int(input())
 a = [int(x) for x in input().split()]
 a.sort()
 su=0
 for i in range(N//2):
  su=su+abs(a[i]-a[N-1-i])
 print(su) 
