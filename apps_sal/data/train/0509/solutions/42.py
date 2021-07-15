from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in list(self.all_group_members().items()))

n, m = list(map(int, input().split()))
un = UnionFind(n)
next_edge_dic = {}
flag = False
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    u -= 1
    v -= 1
    if not un.same(u, v):
        if u not in next_edge_dic:
            next_edge_dic[u] = []
        next_edge_dic[u].append([v, c])
        if v not in next_edge_dic:
            next_edge_dic[v] = []
        next_edge_dic[v].append([u, c])
        un.union(u, v)
    if un.size(0) == n:
        flag = True
        break
if not flag:
    print('No')
else:
    stack = [0]
    visited = set([0])
    ans = [0] * n
    ans[0] = 1
    while stack:
        edge = stack.pop()
        for next_edge, label in next_edge_dic[edge]:
            if next_edge in visited:
                continue
            if ans[edge] == label:
                if label == 1:
                    ans[next_edge] = 2
                else:
                    ans[next_edge] = 1
            else:
                ans[next_edge] = label
            stack.append(next_edge)
        visited.add(edge)
    for i in range(n):
        print((ans[i]))


