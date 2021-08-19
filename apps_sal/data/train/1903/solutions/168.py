class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        # prim O(N^2)
        inf = float('inf')
        n = len(A)
        cost_sum = 0
        nearest_points = [inf]
        for i in range(1, n):
            nearest_points.append(abs(A[i][0] - A[0][0]) + abs(A[i][1] - A[0][1]))
        for i in range(n - 1):
            mn_cost = inf
            for j in range(n):
                if nearest_points[j] < mn_cost:
                    mn_cost = nearest_points[j]
                    mn_cost_index = j
            cost_sum += mn_cost
            nearest_points[mn_cost_index] = inf
            for j in range(n):
                if nearest_points[j] != inf:
                    nearest_points[j] = min(nearest_points[j], abs(A[mn_cost_index][0] - A[j][0]) + abs(A[mn_cost_index][1] - A[j][1]))
        return cost_sum
