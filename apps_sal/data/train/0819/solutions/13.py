#for _ in range(int(input())):
#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]
mp = lambda :map(int,input().split())

import math
for _ in range(int(input())):
    x,y = mp()
    if math.gcd(x,y)==1:
        print("YES")
    else:
        print("NO")
