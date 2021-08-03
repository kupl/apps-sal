class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = list(map(int, input().split()))

S = list(map(int, input().split()))

ans = 0
TA = []
TB = []
for i in range(M):
    a, b = list(map(int, input().split()))
    TA.append(a)
    TB.append(b)

uni = UnionFind(N)
for i in range(M):
    uni.union(TA[i], TB[i])


for i in range(N):
    if uni.same_check(i + 1, S[i]) == True:
        ans += 1
        # print("mohu",i)


print(ans)
