from collections import defaultdict
import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


mod = 10**9 + 7


"""
A,Bの2つのグループに分ける．各グループ内の全ての点へ最短距離が1となる.
逆に，最短距離が1出なければ異なるグループに配属される.
全点間距離はわーシャルフロイトで求める．
これは2-SATかな，a,bの距離が1ではない→a,bは違うグループに入る→(a∨b)∧(not_a ∨ not_b)
これを∧でつなげていけば良い．

どちらに入っても良い点(全ての点との距離が1)，というのがある，これはA,Bの個数のバランスを見て，少ない方に入れていく．
これは2SATだと01のどちらでも良い値になってしまうので計算から予め避けておく.


これ以外にも気をつけるパターンがあって，
aとb,aとc
dとe,dとf
が同じ場所にならないという条件のとき，
aef-bcd
のおように分けたいが
ad-bcef
のようにも分けられてしまう．

ufとかで上手い感じに管理できるかな?
"""


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
            root = self.find(i)
            dd[root].append(i)
        return dd


class Scc_graph:

    def __init__(self, N):
        self.N = N
        self.edges = []

    def csr(self):
        start = [0] * (self.N + 1)
        elist = [0] * len(self.edges)
        for v, w in self.edges:
            start[v + 1] += 1
        for i in range(1, self.N + 1):
            start[i] += start[i - 1]
        counter = start.copy()
        for v, w in self.edges:
            elist[counter[v]] = w
            counter[v] += 1
        self.start = start
        self.elist = elist

    def add_edge(self, v, w):
        self.edges.append((v, w))

    def scc_ids(self):
        self.csr()
        N = self.N
        now_ord = group_num = 0
        visited = []
        low = [0] * N
        order = [-1] * N
        ids = [0] * N
        parent = [-1] * N
        stack = []
        for i in range(N):
            if order[i] == -1:
                stack.append(~i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if v >= 0:
                        if order[v] == -1:
                            low[v] = order[v] = now_ord
                            now_ord += 1
                            visited.append(v)
                            for i in range(self.start[v], self.start[v + 1]):
                                to = self.elist[i]
                                if order[to] == -1:
                                    stack.append(~to)
                                    stack.append(to)
                                    parent[to] = v
                                else:
                                    low[v] = min(low[v], order[to])
                    else:
                        v = ~v
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = N
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x

        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)
        return groups


class Two_sat:
    def __init__(self, N):
        self.N = N
        self.answer = []
        self.scc = Scc_graph(2 * N)

    """
    A[i]=a,A[j]=b
    (a∨b)を追加したいとき，(f,g)=(1,1)
    否定したものを入れたい時fやgを0に変更する
    """

    def add_clause(self, i, f, j, g):
        # assert 0 <= i < self.N
        # assert 0 <= j < self.N
        self.scc.add_edge(2 * i + (f == 0), 2 * j + (g == 1))
        self.scc.add_edge(2 * j + (g == 0), 2 * i + (f == 1))

    def satisfiable(self):
        _, ids = self.scc.scc_ids()
        self.answer.clear()
        for i in range(self.N):
            if ids[2 * i] == ids[2 * i + 1]:
                self.answer.clear()
                return False
            self.answer.append(ids[2 * i] < ids[2 * i + 1])
        return True

# def warshall_floyd(d):
#     #d[i][j]: iからjへの最短距離
#     N=len(d)
#     for k in range(N):
#         for i in range(N):
#             for j in range(N):
#                 d[i][j] = min(d[i][j],d[i][k] + d[k][j])
#     return d
#################################################


N, M = MI()
inf = N + 5
d = [[inf] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0

for _ in range(M):
    a, b = MI()
    a -= 1
    b -= 1
    d[a][b] = 1
    d[b][a] = 1

# 距離が1か否かだけわかれば良いので，これいらない
# d=warshall_floyd(d)

# for i in range(N):
#     print(d[i])


def calc(x):
    return (x * (x - 1)) // 2


uf = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if d[i][j] > 1:
            uf.union(i, j)
            # print(i,j)

roots = uf.roots()
Nr = len(roots)
G = [[]for _ in range(Nr)]

dd = defaultdict(int)
cnt = 0
for v in roots:
    dd[v] = cnt
    cnt += 1

# print(roots,Nr)

for i in range(N):
    r = uf.find(i)
    rnum = dd[r]

    # print(i,r,rnum)
    G[rnum].append(i)


allOK = 0  # A,Bどちらのグループに入れても問題ないもの

"""
とりあえず，連結成分毎に2SATする．
a個,b個(a<=b)
のグループに分けられるとして，これをA,Bのグループにどうふり分けるか.
= (a,b)2つの数字の組みが大量にあって，それらを振り分けて差が小さくなるように頑張れば良いはず

両方にaを加算して，差分(b-a)を記憶しておき，あとでどっちに振り分けるか考える
"""
D = []  # A,Bグループの差
S1 = 0
S2 = 0


for g in G:
    Ng = len(g)
    if Ng == 1:
        allOK += 1
        continue

    g.sort()
    ts = Two_sat(Ng)

    # print(g)

    for i in range(Ng):
        for j in range(i + 1, Ng):
            a = g[i]
            b = g[j]
            if d[a][b] != 1:
                ts.add_clause(i, 0, j, 0)
                ts.add_clause(i, 1, j, 1)

    if not ts.satisfiable():
        print((-1))
        return

    a = sum(ts.answer)
    b = Ng - a

    S1 += min(a, b)
    S2 += min(a, b)

    if a != b:
        D.append(abs(a - b))


# あとはDをどう割り振るか．
# これは，D内の数字を+/-のどちらか符号を選んで足していき，その結果を0に近づけたいという問題に帰着．数字が小さいのでdpでできる.
Nd = len(D)

geta = 1000
dp = [[0] * (geta * 2 + 1) for _ in range(Nd + 1)]
dp[0][geta] = 1
for i, num in enumerate(D):
    for j in range(geta * 2 + 1):
        if dp[i][j]:
            dp[i + 1][j - num] = 1
            dp[i + 1][j + num] = 1

diff = geta
for j in range(geta + 1):
    if dp[-1][j]:
        diff = min(diff,
                   abs(j - geta))

# print(D)
# print(diff)

Sd = sum(D)
s11 = (Sd - diff) // 2
s12 = Sd - s11


# S1<=S2
S1 += s11
S2 += s12

ds = S2 - S1
if ds > allOK:
    ans = calc(S2) + calc(S1 + allOK)
else:
    aa = N // 2
    bb = N - aa
    ans = calc(aa) + calc(bb)


#
print(ans)
