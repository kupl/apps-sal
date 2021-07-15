import math
def f(b,n):
    if b==2: return '01'[n]
    else:
        if n>=b//2: return '1'+f(b//2,b//2-1-(n-b//2))
        else: return '0'+f(b//2,n)
def mystery(n):
    if n==0: return 0
    b=2**(int(math.log(n,2))+1)
    a=f(b,n)
    return (int(a,2))
    

def mystery_inv(n):
    if n==0: return 0
    s=bin(n)[2:]
    x=0
    for i in range(len(s)):
        if int(s[len(s)-1-i]): x=(2**i)+(2**i-1-x)
    return x 
def name_of_mystery():
    return 'Gray code'
