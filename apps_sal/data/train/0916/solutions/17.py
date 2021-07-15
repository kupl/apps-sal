def gcd(n,m):
    if n==0:
        return m
    return gcd(m%n,n)

def lcm(n,m):
    return int((n*m)/gcd(n,m))

for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    print(lcm(n,m))

