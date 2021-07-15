#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
#import io,os; input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline #for     pypy
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

for _ in range(inp()):
 s = input().strip()
 dt = {}
 for i in s: dt[i] = dt.get(i,0)+1
 print(len(dt))
