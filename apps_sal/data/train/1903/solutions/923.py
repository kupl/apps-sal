class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        def dist(a, b):
            return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append([dist(points[i], points[j]), i, j])
        edges.sort()
        st = set()
        ans = 0

        root_ = [i for i in range(len(points))]
        comp = [1 for i in range(len(points))]

        def root(i):
            while root_[i] != i:
                i = root_[i]
            return i

        def union(i, j):
            if root(i) == root(j):
                return
            else:
                rooti = root(i)
                rootj = root(j)

                if comp[rooti] > comp[rootj]:
                    root_[rootj] = rooti
                    comp[rooti] += comp[rootj]
                else:
                    root_[rooti] = rootj
                    comp[rootj] += comp[rooti]

        for i in edges:
            if root(i[1]) == root(i[2]):
                continue
            else:
                union(i[1], i[2])
                ans += i[0]
        return ans
