class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        pairwise_dist = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pairwise_dist.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        pairwise_dist.sort(key=lambda x: x[0])
        distance = 0
        par = list(range(num_points))
        rank = [0] * num_points

        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]

        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if rank[par_x] > rank[par_y]:
                par[par_y] = par_x
            elif rank[par_x] < rank[par_y]:
                par[par_x] = par_y
            else:
                par[par_x] = par_y
                rank[par_y] += 1
        for pair in pairwise_dist:
            if find(pair[1]) == find(pair[2]):
                continue
            distance += pair[0]
            union(pair[1], pair[2])
        return distance
