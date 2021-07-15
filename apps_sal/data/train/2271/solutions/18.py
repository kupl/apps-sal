class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
 
    def root(self, x): #root(x): xの根ノードを返す．
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 
 
    def merge(self, x, y): #merge(x,y): xのいる組とyのいる組をまとめる
        x, y = self.root(x), self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y=y,x #xの要素数が大きいように
        self.size[x] += self.size[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        return True
 
    def issame(self, x, y): #same(x,y): xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def getsize(self,x): #size(x): xのいるグループの要素数を返す
        return self.size[self.root(x)]

# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n = int(readline())
n,m = list(map(int,readline().split()))
*p, = list(map(int,readline().split()))

UF = UnionFind(n)
for _ in range(m):
    x,y = list(map(int,readline().split()))
    UF.merge(x-1,y-1)

q = [set() for _ in range(n)]    
r = [set() for _ in range(n)]    

for i in range(n):
    v = UF.root(i)
    q[v].add(i)
    r[v].add(p[i]-1)

#print(q,r)
ans = 0
for i in range(n):
    ans += len(q[i]&r[i])
    #print(q[i]&r[i])

print(ans)





