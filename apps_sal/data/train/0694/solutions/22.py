# cook your dish here
t = int(input())

def gcd(a,b): 
 if a == 0: 
  return b 
 return gcd(b % a, a) 
 
def lcm(a,b): 
 return (a*b) / gcd(a,b) 
 

for _ in range(t):
 n = int(input())
 x,y,z = map(int,input().split(' '))
 count = 0
 
 p = lcm(x,y)
 p = lcm(p,z)
 
 print(int(24*n / p))
