# cook your dish here
# cook your dish here
def gcd(d,s):
 if s==0:
  return d
 else:
  return gcd(s,d%s)
for _ in range(int(input())):
 n,a,k=[int(x) for x in input().split()]
 d = (360*(n-2)-2*a*n)*(k-1)
 s = n*(n-1)
 k = gcd(d,s)
 d = d//k
 s=s//k
 print(d+s*a,s)
