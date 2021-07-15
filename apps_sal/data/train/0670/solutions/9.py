def gcd (a,b):
 if (a == 0):
  return b
 if (b == 0):
  return a
 if (a>b):
  return gcd(a%b,b)
 else:
  return gcd(a,b%a)
for t in range(int(input())): 
 n = int(input())
 a = list(map(int,input().split()))
 g = a[0]
 for i in range(1,n):
  g = gcd(a[i],g)
  if (g==1):
   break
 print(g*n)

