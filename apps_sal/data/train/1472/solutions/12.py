#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

n = inp()
a,b = 0,0
from functools import reduce
cal = lambda i: reduce((lambda x,y: x*y),map(int,i))
for i in range(1,10**6+1):
    t = str(i)
    if '0' not in t:
        if cal(t) == n:
            if '1' in t:
                b += 1
            else:
                a += 1
print(a,b)
