def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

# Function to return LCM of two numbers 
def lcm(a): 
    res = 1
    for i in range(len(a)):
      res = res*a[i]//gcd(res,a[i])
    return res

for _ in range(int(input())):
  n = int(input())
  p = list(map(int,input().split()))
  r = int(input())
  print(lcm(p)+r)
