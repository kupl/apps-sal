class Solution:
    def find(self, parents, i):
        if parents[i] == -1:
            return i
        return self.find(parents, parents[i])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((i, j))

        def distance(i, j):
            p1, p2 = points[i], points[j]
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        pairs = sorted(pairs, key=lambda pair: distance(pair[0], pair[1]))

        total = 0
        parents = [-1] * n
        countE = 0
        for pair in pairs:
            if countE >= n - 1:
                break
            i, j = pair
            pi = self.find(parents, i)
            pj = self.find(parents, j)
            if pi == pj:
                continue

            parents[pi] = pj
            total += distance(i, j)
            countE += 1
        return total
