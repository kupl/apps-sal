class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 先算每一对点的距离
        # 最小生成树, union find
        edges = []
        n = len(points)
        if n == 1:
            return 0
        for i in range(n - 1):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, dist))
        edges.sort(key = lambda x : x[2])
        parent = [i for i in range(n)]
        cnt = 0
        ans = 0
        for e in edges:
            x = e[0]
            y = e[1]
            px = self.find(x, parent)
            py = self.find(y, parent)
            if px != py:
                parent[px] = py
                cnt += 1
                ans += e[2]
            if cnt == n - 1:
                break
        return ans
        
    def find(self, x, parent):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
