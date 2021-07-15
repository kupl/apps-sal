# cook your dish here
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//(gcd(x,y))


abc="abcdefghijklmnopqrstuvwxyz"

pi=3.141592653589793238




t = int(input())
for _ in range(t):
    k = int(input())
    k_buf = k*1
    n_lines = k + 1
    for i in range(n_lines):
        buf = " "*k
        for j in range(k,k_buf+1):
            buf=buf+str(j)
        k = k - 1
        print(buf)
    for i in range(1,k_buf+1):
        buf=" "*i
        for j in range(i,k_buf+1):
            buf = buf+str(j)
        print(buf)
    
    
    

