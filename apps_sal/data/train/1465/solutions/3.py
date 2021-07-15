import sys

def powc(x,n,m):
  res = 1
  xx=x
  while n:
    if n&1:
      res = (res*xx)%m
    xx=xx*xx%m
    n >>= 1
  return res

def findRoot():
  S = [(0,-1)]
  for u in S:
    for w in V[u[0]]:
      if w[0]!=u[1]:
        S.append((w[0],u[0]))
  S = [(S[-1][0],-1,0)]
  D = [0]*n
  for u in S:
    for w in V[u[0]]:
      if w[0]!=u[1]:
        D[w[0]]=u[2]+1
        S.append((w[0],u[0],u[2]+1))
  d = S[-1][2]
  size = d
  u = S[-1][0]
  while size/2<d:
    for w in V[u]:
      if D[w[0]]+1==D[u]:
        u = w[0]
        d -= 1
        break 
  return u
  
class Node:
  def __init__(self, value, edge, parent = None):
    self.value = value
    self.edge = edge
    if parent:
      parent.addChild(self)
    else:
      self.parent = None
    self.children = []
  def addChild(self, node):
    node.parent = self
    self.children.append(node)
  def __repr__(self):
    r = repr(self.value)
    for v in self.children:
      r += ' ' + repr(v)
    return r


def hangTree(root):
  global NodesArray
  NodesArray = [None]*n
  S=[(root, Node(root,-1),-1)]
  NodesArray[root] = S[0][1]
  for u in S:
    for v in V[u[0]]:
      if v[0] != u[2]:
        node = Node(v[0],v[1],u[1])
        NodesArray[v[0]] = node
        S.append((v[0],node,u[0]))

def findPath2(u,v):
  n0 = NodesArray[u]
  n1 = NodesArray[v]
  q = [0]*n
  while n0.parent:
    q[n0.edge] ^= 1
    n0 = n0.parent
  while n1.parent:
    q[n1.edge] ^= 1
    n1 = n1.parent
  return q
         
T = int(sys.stdin.readline())
for _ in range(T):
  n,Q = list(map(int,sys.stdin.readline().split()))
  V = list(map(list,[[]]*n))
  W = [0]*n
  for i in range(n-1):
    u,v = list(map(int,sys.stdin.readline().split()))
    u-=1
    v-=1
    V[u].append((v,i))
    V[v].append((u,i))
    W[u] += 1
    W[v] += 1
  easy = n==1
  root = findRoot()
  hangTree(root)
  M = []
  for _ in range(Q):
    u,v,x = list(map(int,sys.stdin.readline().split()))
    if not easy:
      q = findPath2(u-1,v-1)
      q[-1] = x
      M.append(q)
  if easy:
    print(1)
    continue
  empty = [0]*n
  bad = [0]*n
  bad[-1] = 1
  is_there_bad = False
  empty_cnt = 0
  i = 0
  for q in M:
    i += 1
    if q == empty:
      empty_cnt += 1
      continue
    if q == bad:
      is_there_bad = True
      break
    o = q.index(1)
    for next in range(i,Q):
      if M[next][o]==1:
        for k in range(n):
          M[next][k] ^= q[k]
  if is_there_bad:
    print(0)
  else:
    print(powc(2,n-1-Q+empty_cnt,10**9+7))

