def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
def lcm(a, b):
    return (a / gcd(a, b)) * b
t=int(input())
for items in range(t):
    n,y=list(map(int,input().split()))
    if n==y:
        print('0')
    else:
        ans=lcm(n,y)
        first=(ans-n)//n
        second=(ans-y)//y
        print(int(first+second))

