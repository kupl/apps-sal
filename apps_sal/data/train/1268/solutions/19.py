from math import gcd

def sap(n, a, d):
 return n*(2*a + (n-1) * d)//2

while True:
 n, m, x = map(int, input().split())
 if m is 0:
  break
 c = gcd(n, m)
 l = m//c
 ans = (sap(m, x, n) - c * sap(l, x % c, c))//m
 print(ans)
