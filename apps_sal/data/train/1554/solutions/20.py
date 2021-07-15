t = int(input())

def gcd(a, b):
 if(b==0):
  return a
 else:
  return gcd(b, a%b)

for _ in range(t):
 x, y = [int(a) for a in input().split()]
 
 print(gcd(x, y)*2)
