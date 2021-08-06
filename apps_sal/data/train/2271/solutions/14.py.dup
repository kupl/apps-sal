n, m = map(int, input().split())
P = [i - 1 for i in list(map(int, input().split()))]


class UnionFind():
    def __init__(self, num):
        self.n = num  # class内変数nに、外部から入力した値numを代入
        self.parents = [-1 for i in range(self.n)]
        # parentsは要素の親(1こ上のやつ)番号0~n-1を格納、自分が最親なら-(要素数)を格納(初期値は-1)

    # xの最親は誰？
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])  # 再帰して1番上までいってる
            # 調べながらparentsの値を更新してる！（経路圧縮）
            return self.parents[x]

    # 結合せよ
    # xの親とyの親をくっつける
    def union(self, x, y):
        xx = self.find(x)  # xxはxの最親
        yy = self.find(y)  # yyはyの最親
        if xx == yy:
            return  # 同じ屋根の下にあった場合は何もしない
        else:
            size_xx = abs(self.parents[xx])  # xが含まれる木のサイズ
            size_yy = abs(self.parents[yy])  # yが含まれる木のサイズ
            if size_xx > size_yy:
                xx, yy = yy, xx  # yyの方が大きい木、ってことにする

            self.parents[yy] += self.parents[xx]  # 大きい木のサイズ更新
            self.parents[xx] = yy  # サイズが小さい木を大きい木に接ぐ

    # xの属する木の大きさ（まあunionでも使ったけど）
    def size(self, x):
        xx = self.find(x)
        return abs(self.parents[xx])

    # xとyはこの空の続く場所にいますか　いつものように笑顔でいてくれますか　今はただそれを願い続ける
    def same(self, x, y):
        return 1 if self.find(x) == self.find(y) else 0

    # xと　同じ木にいる　メンバーは？
    def members(self, x):
        xx = self.find(x)
        return [i for i in range(self.n) if self.find(i) == xx]
        # ifの条件式に漏れたら無視

    # 最親だけを並べあげる
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
        # いやこれは天才すぎる、basisのenumerate.py参照

    # すべての最親について、メンバーを辞書で
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    # グループ分けどうなりましたか、２重リストで
    def state_grouping(self):
        return list(self.all_group_members().values())


uf = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)
ans = 0
for i in range(n):
    ans += uf.same(i, P[i])
print(ans)
