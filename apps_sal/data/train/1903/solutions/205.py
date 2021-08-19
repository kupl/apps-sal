class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def minKey(keys, mstSet):
            min_value = float('+Inf')
            for v in range(len(points)):
                if keys[v] < min_value and (not mstSet[v]):
                    min_value = keys[v]
                    min_index = v
            return (min_index, min_value)

        def get_distance(u, v):
            return abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
        (size, total) = (len(points), 0)
        keys = [float('+Inf')] * size
        keys[0] = 0
        mstSet = [False] * size
        for i in range(size):
            (u, min_value) = minKey(keys, mstSet)
            total += min_value
            mstSet[u] = True
            for v in range(size):
                distance = get_distance(u, v)
                if keys[v] > distance > 0 and mstSet[v] == False:
                    keys[v] = distance
        return total
