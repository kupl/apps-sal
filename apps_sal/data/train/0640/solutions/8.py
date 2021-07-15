# cook your dish here
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
def lcm(a,b):
    return (a / gcd(a,b))* b
T=int(input())
for i in range(T):
    init=list(map(int, input().split()))
    X=init[0]
    Y=init[1]
    q=lcm(X,Y)
    t1=q/X
    t2=q/Y
    print(int(t1+t2-2))
