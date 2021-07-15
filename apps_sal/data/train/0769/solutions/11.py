def gcd(x, y):
 if x==0:
  return y
 return gcd(y%x, x)
for _ in range(int(input())):
 a, b=map(int, input().split())
 print(gcd(a, b))
