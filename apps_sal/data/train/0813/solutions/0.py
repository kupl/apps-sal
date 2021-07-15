#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

n,k = ip()
x = ip()
x.sort()
if k == 1:
    a = x[n//2]
    b = x[n//2-1]
else:
    s = sum(x)
    a = s//n
    b = a + 1
sa = sum([abs((a-i)**k) for i in x])
sb = sum([abs((b-i)**k) for i in x])
if sa < sb:
    print(a)
else:
    print(b)
