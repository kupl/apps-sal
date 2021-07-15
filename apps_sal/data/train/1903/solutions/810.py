class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = [[] for _ in range(n)]
        
        for i, point in enumerate(points):
            for j, other in enumerate(points):
                dist = abs(point[0] - other[0]) + abs(point[1] - other[1])
                distances[i].append((dist, j))
                distances[j].append((dist, i))
        
        for i in range(n):
            distances[i].sort()
        
        conn = set()
        idxes = [0] * n
        conn.add(0)
        res = 0
        cur = [0]
        
        while len(cur) < n:
            min_dist = 10000000
            min_point = (0, 0)
            for point in cur:
                while distances[point][idxes[point]][1] in conn:
                    idxes[point] += 1
                if distances[point][idxes[point]][0] < min_dist:
                    min_dist = distances[point][idxes[point]][0]
                    min_point = (point, distances[point][idxes[point]][1])
            conn.add(min_point[1])
            cur.append(min_point[1])
            res += min_dist
        return res
