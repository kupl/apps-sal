class UF:
    def __init__(self):
        self.ranks = collections.defaultdict(int)
        self.p = collections.defaultdict(int)

    def union(self, i, j):
        ip, jp = self.find(i), self.find(j)
        if ip == jp:
            return False

        # // ranking
        if self.ranks[ip] < self.ranks[jp]:
            ip, jp = jp, ip
        self.ranks[ip] += self.ranks[jp]

        self.p[jp] = ip
        return True

    def find(self, i):
        if i not in self.p:
            self.ranks[i] = 1
            self.p[i] = i
            return i
        if i != self.p[i]:
            # path compression
            self.p[i] = self.find(self.p[i])
        return self.p[i]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        from queue import PriorityQueue
        q = PriorityQueue()
        seen = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                md = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                q.put((md, i, j))

        uf = UF()
        res = 0
        count = 0
        while q.qsize() > 0:
            md, i, j = q.get()
            if uf.union(i, j):
                seen.add(i)
                seen.add(j)
                res += md
                count += 1
            if count == len(points) - 1:
                break

        return res
