from heapq import heappush, heappop
N,Q,*L = map(int, open(0).read().split())
D = L[3*N:]
ls = []
for i in range(N):
  s,t,x = L[3*i],L[3*i+1],L[3*i+2]
  ls.append((s-x,1,x))
  ls.append((t-x,0,x))
for i,d in enumerate(D):
  ls.append((d,2,i))
ls.sort()
ans = [0]*Q
S = set()
hq = []
for a,b,c in ls:
  if b==0:
    S.remove(c)
  elif b==1:
    S.add(c)
    heappush(hq,c)
  else:
    while hq and hq[0] not in S:
      heappop(hq)
    ans[c] = hq[0] if hq else -1
print('\n'.join(map(str,ans)))
