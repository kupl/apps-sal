class Solution:

    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        else:
            self.rank[x] += 1
            self.parent[y] = x

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        ans = 0
        if l > 1:
            heap = list()
            for i in range(l - 1):
                self.parent[i] = i
                self.rank[i] = 0
                for j in range(i + 1, l):
                    heap.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
            self.parent[l - 1] = l - 1
            self.rank[l - 1] = 0
            heapq.heapify(heap)
            while heap:
                (dis, x, y) = heapq.heappop(heap)
                if self.find(x) != self.find(y):
                    ans += dis
                    self.union(self.find(x), self.find(y))
        return ans
