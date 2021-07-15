#cook your dish here
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
    
def lcm(a,b): 
    return (a*b) // gcd(a,b) 
    
for _ in range(int(input())):
    m, n = map(int,input().split())
    print(lcm(m,n))
