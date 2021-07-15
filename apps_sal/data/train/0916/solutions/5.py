# cook your dish here
t = int(input())

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  

def lcm(a,b): 
    return (a*b) // gcd(a,b) 

for i in range(t):
    n,m = map(int, input().split())
    print(lcm(n,m))
