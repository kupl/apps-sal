# cook your dish here
def gcd(a,b):
 a,b=max(a,b),min(a,b)
 while b!=0:
  a,b=b,a%b
 return a
for a0 in range(int(input())):
 a,b=list(map(int, input().split()))
 print(gcd(a,b))
