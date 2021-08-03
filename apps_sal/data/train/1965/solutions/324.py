class DisjointSet():
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(0, n):
            self.parent[i] = i

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 0
        else:
            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            elif self.rank[y_parent] > self.rank[x_parent]:
                self.parent[x_parent] = y_parent
            else:
                self.parent[y_parent] = x_parent
                self.rank[x_parent] += 1
            return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res = e1 = e2 = 0
        ds = DisjointSet(n)
        print((ds.parent))
        for t, u, v in edges:
            if t == 3:
                if ds.union(u - 1, v - 1):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        print((ds.parent))

        tmp = copy.deepcopy(ds)
        for t, u, v in edges:
            if t == 1:
                if ds.union(u - 1, v - 1):
                    e1 += 1
                else:
                    res += 1

        for t, u, v in edges:
            if t == 2:
                print()
                if tmp.union(u - 1, v - 1):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1
