a2n=lambda x:ord(x)-ord('a')
# 数値(1〜26)→アルファベット(a〜z)
n2a = lambda x:chr(x+ord('a')).lower()

s=list(map(a2n,list(input())))
n=len(s)
cary=[0]*26
from collections import deque
ary=[deque([]) for _ in range(26)]
for i,x in enumerate(s):
  cary[x]+=1
  ary[x].append(i)
oddcnt=0
for x in cary:
  if x%2==1:oddcnt+=1
if oddcnt>1:
  print(-1)
  return

# 0-indexed binary indexed tree
class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0]*(n+1)
    self.el = [0]*(n+1)
  # sum of [0,i) sum(a[:i])
  def sum(self, i):
    if i==0:return 0
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    i+=1
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  # sum of [l,r)   sum(a[l:r])
  def sumlr(self, i, j):
    return self.sum(j) - self.sum(i)
  # a[i]
  def get(self,i):
    i+=1
    return self.el[i]

bit=BIT(n)
for i in range(n):
  bit.add(i,1)
ans=0
m=n
for i in range(n//2):
  # idx=i,n-1-iにくるものを考える
  t=-1
  v=float('inf')
  for j in range(26):
    if not ary[j]:continue
    l=ary[j][0]
    r=ary[j][-1]
    tmp=0
    # lからiへ
    tmp+=bit.sum(l)
    # rからn-1-iへ
    tmp+=m-2*i-bit.sum(r+1)
    if v>tmp:
      v=tmp
      t=j
  r=ary[t].pop()
  l=ary[t].popleft()
  bit.add(l,-1)
  bit.add(r,-1)
  ans+=v
print(ans)
