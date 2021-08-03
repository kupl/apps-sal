class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [inf] * len(points)
        tree = [0] * len(points)

        idx = 0
        result = 0
        for i in range(len(points) - 1):
            tree[idx] = 1

            min_dist_idx = 0
            for j in range(len(points)):
                if tree[j] == 1:
                    continue

                point = points[j]
                distance = abs(point[0] - points[idx][0]) + abs(point[1] - points[idx][1])
                if dist[j] > distance:
                    dist[j] = distance
                if dist[min_dist_idx] > dist[j]:
                    min_dist_idx = j
            idx = min_dist_idx
            print((dist[min_dist_idx]))
            result += dist[min_dist_idx]
        return result
