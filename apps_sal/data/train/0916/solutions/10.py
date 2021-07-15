from fractions import gcd
try:
    def lcm(x, y):
        return x * y // gcd(x, y)
    tc=int(input())
    for _ in range(tc):
        x,y=map( int,input().split() )
        print(lcm(x,y))
except:
    pass
