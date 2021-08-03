class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        not_added = set([i for i in range(1, len(points))])
        distance_to_added = [math.inf for i in range(len(points))]
        i = 0
        res = 0
        while not_added:
            for j in not_added:
                distance_to_added[j] = min(distance_to_added[j], distance(i, j))
            while not_added:
                i = min(range(len(points)), key=lambda x: distance_to_added[x])
                if i in not_added:
                    res += distance_to_added[i]
                    not_added.remove(i)
                    break
                distance_to_added[i] = math.inf
        return res
