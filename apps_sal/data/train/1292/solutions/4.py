#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

n,m,w,b,*g = ip()
dt = {i:[] for i in range(1,n+1)}
for i in range(0,2*w,2):
 dt[g[i]].append([g[i+1],'W'])
g = g[2*w:]
for i in range(0,2*b,2):
 dt[g[i]].append([g[i+1],'B'])
ans = 0
for i in range(1,n+1):
 t = sorted(dt[i])
 if t == [] or t[-1][0] != m:
  t.append([m,'B'])
  ans += 1
 else:
  t[-1][1] = 'B'
 prev = 1
 for j in range(len(t)):
  ind,cell = t[j]
  no = ind - prev
  if cell == 'B':
   l = 2
   r = ind - prev + 1
  else:
   nxt = t[j+1][0]
   l = nxt - ind + 2
   r = nxt - prev + 1
  ans += no*(l+r)//2
  prev = ind + 1
print(ans)







 

