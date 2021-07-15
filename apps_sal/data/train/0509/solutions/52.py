import sys
sys.setrecursionlimit(10**8)

class union_find:
  def __init__(self, n):
    self.par = [-1] * n

  def find(self, x):#xの親を見つける
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self,x,y):#要素xとｙを併合させる
    x,y=self.find(x),self.find(y)#xとyの親の検索
    if x!=y:#親が異なる場合併合させる
      if x>y:
        x,y=y,x#小さい方をxとする. これにより要素の値が小さいものを優先して木の根とする. 
      self.par[x]+=self.par[y] #値を無向木の要素数の和にする.
      self.par[y]=x #枝側は根の位置を格納

  def same(self, x, y):#要素xと要素yが同じ無向木に所属しているかを判定する
    return self.find(x) == self.find(y)#同じ値を持つか否か

  def size(self, x):#要素xが所属する無向木の大きさを返す
    return-self.par[self.find(x)]
  
n, m = map(int, input().split())
gragh = [[] for _ in range(n)]
ans = [-1]*n
def dfs(now):
  for nex, c in gragh[now]:
    if ans[nex] != -1:continue
    if ans[now] == c:
      ans[nex] = (c+1)%n + 1
    else:
      ans[nex] = c
    dfs(nex)
    
def main():
  tree = union_find(n)
  for i in range(m):
    u, v, c = map(int, input().split())
    if not tree.same(u-1, v-1):
      tree.unite(u-1, v-1)
      gragh[u-1].append([v-1, c])
      gragh[v-1].append([u-1, c])
  ans[0] = 1
  dfs(0)
  for i in ans:
    print(i)
    
def __starting_point():
  main()
__starting_point()
