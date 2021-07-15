import heapq
# v:頂点数, s:始点, path[i]:[[cost,to]...] i=fromの隣接リスト
def dijkstra(v,s,path):
    inf = float('inf')

    # 距離をinfで初期化
    d = [inf for i in range(v)]
    d[s] = 0

    # sへの距離は0
    q = [[0,s]]
    heapq.heapify(q)

    # 距離が最小の頂点から更新していけば
    # p[1]から行ける
    while q:
        p = heapq.heappop(q)

        # 頂点p[1]までの距離がheapないのp[1]までの距離より小さい場合、continue
        if d[p[1]]<p[0]:
            continue

        # 頂点p[1]から伸びる、全ての辺の距離を確認
        for i in range(len(path[p[1]])):
            # 頂点p[1]から行ける頂点の距離がp[1]までの距離とp[1]からの距離の和より小さい場合 -> 距離を更新し、heapに追加
            if d[path[p[1]][i][1]] > d[p[1]] + path[p[1]][i][0]:
                d[path[p[1]][i][1]] = d[p[1]]+path[p[1]][i][0]
                heapq.heappush(q,[d[path[p[1]][i][1]], path[p[1]][i][1]])
    return d

def path_recovery(e,d,path):
    # 経路
    route = [e]
    # 残りの距離
    a = d[e]
    while a!=0:
        for i in range(len(path[e])):
            if d[path[e][i][1]]+path[e][i][0]==a:
                route.append(path[e][i][1])
                a -= path[e][i][0]
                e = path[e][i][1]
                break
    route.reverse()
    return route

class UnionFind:
    # 初期化
    def __init__(self, n):
        # 根なら-size, 子なら親の頂点
        self.par = [-1] * n
        # 木の高さ
        self.rank = [0] * n

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 異なる集合に属する場合のみ併合
        if x != y:
            # 高い方をxとする。
            if self.rank[x] < self.rank[y]:
                x,y = y,x
            # 同じ高さの時は高さ+1
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            # yの親をxとし、xのサイズにyのサイズを加える
            self.par[x] += self.par[y]
            self.par[y] = x

    # 同集合判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 集合の大きさ
    def size(self, x):
        return -self.par[self.find(x)]

n = int(input())

l = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    # dijkstraのlibraryに合わせるため、距離1を追加
    l[a-1].append([1,b-1])
    l[b-1].append([1,a-1])

d = dijkstra(n,0,l)

p = path_recovery(n-1,d,l)

x = p[(len(p)-1)//2]
y = p[(len(p)-1)//2+1]

for i in range(len(l[x])):
    if l[x][i][1]==y:
        l[x].pop(i)
        break
for i in range(len(l[y])):
    if l[y][i][1]==x:
        l[y].pop(i)
        break

u = UnionFind(n)

for i in range(len(l)):
    for j in range(len(l[i])):
        u.unite(i,l[i][j][1])


if u.size(0)>u.size(n-1):
    print('Fennec')
else:
    print('Snuke')
