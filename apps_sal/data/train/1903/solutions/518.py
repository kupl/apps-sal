class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # my gut said a kruskal MST? YES

        N = len(points)
        edge_list = []
        for i in range(N):
            x0, y0 = points[i]
            for j in range(i + 1, N):
                x1, y1 = points[j]
                mh = abs(x1 - x0) + abs(y1 - y0)
                edge_list.append((mh, i, j))
        edge_list.sort()
        # print(edge_list)

        # implement kruskal
        edge_count = 0
        val = 0
        uf = UnionFind(N)

        while(edge_count != N - 1):
            mh, i, j = edge_list.pop(0)

            if(uf.union(i, j)):
                # we're good
                val += mh
                edge_count += 1
            #print(edge_count, val, x0,y0, x1, y1)

        return val


class UnionFind():
    def __init__(self, n):
        self.parents = {i: i for i in range(0, n)}
        self.groups = n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        self.parents[y] = x
        self.groups -= 1
        return True
