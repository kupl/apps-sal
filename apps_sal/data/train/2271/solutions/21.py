class Unionfind():  # Unionfind
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

    def find(self, x):  # グループの根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # グループの併合
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def all_group_members(self):  # グループごとの辞書
        members_dict = {i: set([i]) for i, x in enumerate(self.parents) if x < 0}
        for i, x in enumerate(self.parents):
            if x >= 0:
                members_dict[self.find(x)].add(i)
        return members_dict


n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

uf = Unionfind(n)
for x, y in xy:
    uf.union(x - 1, y - 1)

ans = 0
for lst in list(uf.all_group_members().values()):
    ans += sum((p[num] - 1 in lst) for num in lst)
print(ans)

