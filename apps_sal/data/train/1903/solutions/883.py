
class UnionFind(object):
    def __init__(self, n):
        # * only idff from template is it starts at 0
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)
        if p_root == q_root:
            return False
        if self.rank[p_root] > self.rank[q_root]:
            p_root, q_root = q_root, p_root
        self.parent[p_root] = q_root
        self.rank[q_root] += self.rank[p_root]
        self.count -= 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        g = collections.defaultdict(list)
        n = len(points)
        heap = []
        #create graph
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan(points[i], points[j])
                heap.append((distance, i, j))
        res = 0
        heapq.heapify(heap)
        while heap:
            weight, i, j = heapq.heappop(heap)
            if uf.union(i, j):
                res += weight
        return res
