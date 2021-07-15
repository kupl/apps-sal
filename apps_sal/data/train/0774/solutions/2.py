class union_find:
 def __init__(self,N):
  self.parent = {}
  self.rank = []
  for i in range(N):
   self.parent[i] = i
   self.rank.append(0)

 def find(self,x):
  y = x
  while(x!=self.parent[x]):
   x = self.parent[x]
  self.parent[y] = x
  return x

 def union(self,x,y):
  px = self.find(x)
  py = self.find(y)
  if(px==py):
   return
  else:
   if(self.rank[px]>self.rank[py]):
    self.parent[py] = px
   elif(self.rank[px]<self.rank[py]):
    self.parent[px] = py
   else:
    self.parent[py] = px
    self.rank[px] += 1

N,K,P = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
ans = []

uf = union_find(N)

Y = []
for i in range(N):
 Y.append((X[i],i))
Y.sort()

for i in range(N-1):
 if(Y[i+1][0]-Y[i][0]<=K):
  uf.union(Y[i][1],Y[i+1][1])

A = []
B = []

for i in range(P):
 a,b = [int(i) for i in input().split()]
 A.append(a-1)
 B.append(b-1)

for i in range(P):
 pa = uf.find(A[i])
 pb = uf.find(B[i])
 if(pa==pb):
  ans.append('Yes')
 else:
  ans.append('No')

for i in ans:
 print(i)

