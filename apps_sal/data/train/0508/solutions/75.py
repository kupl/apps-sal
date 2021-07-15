import heapq
# sys.stdin.readline()
import sys
input = sys.stdin.readline

N,Q = list(map(int, input().split()))

S,T,X = [],[],[]

Ev = []
for _ in range(N):
  s,t,x = list(map(int, input().split())) 
  Ev.append((s-x,True,x))
  Ev.append((t-x,False,x))
"""
2 5 6
5 -1
4 2
3 3
2 4
1 5
0 -1
"""
Ev.sort()
#print(Ev)
# C++のSetはminもO(logN)で取れるが、Pythonは無理。
# setとheapqを併用すると計算量が実現できる。
h = []
closed = set()
eidx = 0
D = []

# 受け取った方が早い・・・？
for i in range(Q):
  D.append(int(input()))

for d in D:
  # dはsortedでinputされる。
  #d = int(input())
  #Query.append(d)
  while eidx < 2*N and Ev[eidx][0] <= d:
    #pop
    t,e,x = Ev[eidx]
    eidx += 1
    if e:
      heapq.heappush(h, x)
      closed.add(x)
    else:
      closed.remove(x)
      
  # heqpqの最小値がsetに含まれている間、捨て続ければ、setの要素とheapqの要素が一致する
  while h and h[0] not in closed:
    heapq.heappop(h)
    
  # assert( len(h) == len(set) )
  if h:
    print((h[0]))
  else:
    print((-1))

