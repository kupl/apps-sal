#for _ in range(int(input())):
#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]
mp = lambda :map(int,input().split())
import math

def per(x): 
    s = int(math.sqrt(x))
    return s*s == x 
def isfibo(n): 
    return per(5*n*n + 4) or per(5*n*n - 4)

for _ in range(int(input())):
    x,y = mp()
    if math.gcd(x,y)==1:
        print("YES")
    else:
        print("NO")
