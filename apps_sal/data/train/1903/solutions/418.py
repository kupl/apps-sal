
               
def find_root(parents, i):
    if parents[i] == -1:
        return i
    else:
        return find_root(parents, parents[i])
   
def calc_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
       
        graph = []
        n = len(points)
       
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = calc_dist(points[i], points[j])
                heapq.heappush(graph, [dist, (i, j)])
       
        parents = [-1] * len(points)
        cost = 0
        count = 0
        # print (graph)
        while count < n - 1:
            dist, point_pair = heapq.heappop(graph)
            # print(dist, point_pair)
            p1, p2 = point_pair[0], point_pair[1]
           
            r1 = find_root(parents, p1)
            r2 = find_root(parents, p2)
           
            if r1 != r2:
                parents[r1] = r2
                cost = cost + dist
                count = count + 1
       
        return cost
