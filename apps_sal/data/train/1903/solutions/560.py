class UnionFind:
    def __init__(self, length):
        self.parents = [-1] * length
        self.ranks = [1] * length

    def find(self, src):
        if self.parents[src] == -1:
            return src
        self.parents[src] = self.find(self.parents[src])
        return self.parents[src]

    def union(self, src, dest):
        rootSrc, rootDest = self.find(src), self.find(dest)
        if rootSrc == rootDest:
            return False

        if self.ranks[rootSrc] > self.ranks[rootDest]:
            self.parents[rootDest] = rootSrc
            self.ranks[rootSrc] += self.ranks[rootDest]
            return True
        else:
            self.parents[rootSrc] = rootDest
            self.ranks[rootDest] += self.ranks[rootSrc]
            return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calHamming(pt1, pt2):
            return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

        ptsDistance = []
        for i, j in itertools.combinations(range(len(points)), 2):
            ptsDistance.append((calHamming(points[i], points[j]), i, j))

        ptsDistance.sort()

        result = 0
        uf = UnionFind(len(points))
        for distance, src, dest in ptsDistance:
            if uf.union(src, dest):
                result += distance
        return result
