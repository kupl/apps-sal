#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
#import io,os; input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline #for pypy
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    x = ip()
    dp = [0]*n
    for i in range(n):
        if (i-1)>=0 and x[i] == x[i-1]:
            dp[i] = max(dp[i],dp[i-1]+1)
        if (i-2)>=0 and x[i] == x[i-2]:
            dp[i] = max(dp[i],dp[i-2]+1)
    print(max(dp))
