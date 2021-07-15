import math

def lcm(a, b):
    return (a*b)//gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)    
    
for _ in range(int(input())):
    n = int(input())

    na = math.ceil((2*n)/math.acos(-1))
    nb = ((n+1)//2)**2

    nlcm = lcm(na, nb)

    oa = math.ceil(n/2)
    ob = (n//2)*(n//2+1)

    olcm = lcm(oa, ob)

    if olcm > nlcm:
        print("Nova's gonna kill me")
    else:
        print("YESS(sunglass emo)")

# cook your dish here

