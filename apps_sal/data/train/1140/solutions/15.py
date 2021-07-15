#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

for _ in range(inp()):
 k,ind = ip()
 ans = 0
 while k:
  ans = 2*ans + ind%2
  ind //= 2
  k -= 1
 print(ans)
