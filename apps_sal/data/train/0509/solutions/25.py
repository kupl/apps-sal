import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
mod=10**9+7

"""
基本的に達成可能だと思う
基本は次数が小さいところ(=端)を取れるように頂点の値を決めておけばOk
問題は同じ頂点に入っている複数の辺が同じ数値の場合.この時は端ではない方にその数値を割り振るか?

長さ4のパスで3辺の値がどれも1のときとか

スターグラフが2つ連結している時とかもめんどいな
"""
from collections import defaultdict
class UnionFind:
    def __init__(self, N: int):
        """
        N:要素数
        root:各要素の親要素の番号を格納するリスト.
             ただし, root[x] < 0 ならその頂点が根で-root[x]が木の要素数.
        rank:ランク
        """
        self.N = N
        self.root = [-1] * N
        self.rank = [0] * N

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def find(self, x: int):
        """頂点xの根を見つける"""
        if self.root[x] < 0:
            return x
        else:
            while self.root[x] >= 0:
                x = self.root[x]
            return x

    def union(self, x: int, y: int):
        """x,yが属する木をunion"""
        # 根を比較する
        # すでに同じ木に属していた場合は何もしない.
        # 違う木に属していた場合はrankを見てくっつける方を決める.
        # rankが同じ時はrankを1増やす
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x: int, y: int):
        """xとyが同じグループに属するかどうか"""
        return self.find(x) == self.find(y)

    def count(self, x):
        """頂点xが属する木のサイズを返す"""
        return - self.root[self.find(x)]

    def members(self, x):
        """xが属する木の要素を列挙"""
        _root = self.find(x)
        return [i for i in range(self.N) if self.find == _root]

    def roots(self):
        """森の根を列挙"""
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        """連結成分の数"""
        return len(self.roots())

    def all_group_members(self):
        """{ルート要素: [そのグループに含まれる要素のリスト], ...}のデフォルトディクトを返す"""
        dd = defaultdict(list)
        for i in range(N):
            root=self.find(i)
            dd[root].append(i)
        return dd
    
def Kruskal(maxV, edges):
    edges.sort()
    newAdj=[[]for _ in range(N)]
    uf=UnionFind(maxV)
    ans = 0
    for e in edges:
        fro = e[0]
        to = e[1]
        if uf.find(fro) != uf.find(to):
            uf.union(fro,to)
            ans+=e[0]
            newAdj[fro].append(to)
            newAdj[to].append(fro)
            
    return newAdj

# ラベルを色と呼ぶ

N,M=MI()
from collections import defaultdict
dd = defaultdict(int)
Edge=[]

# 多重辺は無視しても行けそう

for _ in range(M):
    u,v,c=MI()
    u-=1
    v-=1
    c-=1
    if dd[(u,v)]:
        continue
    Edge.append((u,v))
    
    dd[(u,v)]=c
    dd[(v,u)]=c
    
# 木で十分かな
adj=Kruskal(N,Edge)
# print(adj)

Col=[-1]*N

import queue
q=queue.Queue()

for v in adj[0]:
    q.put((v,0))
    

while not q.empty():

    v,p=q.get()
    
    if Col[p]!=dd[(v,p)]:#親を繋げられてないなら
        Col[v]=dd[(v,p)]
    else:
        #親とつなげるためには違う色である必要あり
        if Col[p]==0:
            Col[v]=1
        else:
            Col[v]=0
        
    for nv in adj[v]:
        if nv==0 or Col[nv]!=-1:
            continue
        q.put((nv,v))
        
# rootの色を決める，隣接色以外
col_0=[0]*N
for v in adj[0]:
    col_0[Col[v]]+=1
    
for i in range(N):
    if col_0[i]==0:
        Col[0]=i
        break
# print(col_0)

for i in range(N):
    print((Col[i]+1))




