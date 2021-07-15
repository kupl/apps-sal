# your code goes here
def gcd(a,b):
 if b==0:
  return a
 else:
  return gcd(b,a%b)
  
t=int(input().strip())
while t:
 a=int(input().strip())
 b=a*4
 a+=1
 ans=b/gcd(b,a)
 print(ans)
 t-=1
