from fractions import gcd
for _ in range(int(input())):   
 n = int(input())
 a = list(map(int, input().split()))
 res = a[0]
 for i in a[1:]:
  res= gcd(res, i)
 print(res * len(a)) 
