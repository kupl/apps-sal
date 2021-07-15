from fractions import gcd

def DPC_sequence(s):
    n=1
    for i,c in enumerate(s,1):
        if c=='D':
            n=(n*i)//gcd(n,i)
        elif c=='P':
            if gcd(n,i)!=1: return -1
        elif c=='C':
            if gcd(n,i) in (1,i): return -1
    return n

