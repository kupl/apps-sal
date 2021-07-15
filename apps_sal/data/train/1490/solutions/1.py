#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    x = ip()
    dt = {} 
    for i in x: dt[i] = dt.get(i,0)+1
    ans = max(max(dt.values()),(n-1)//2+1)
    print(ans)
