class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        if len(points) == 1:
            return 0
        heap = []
        group = {i:i for i in range(len(points))}
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                heap.append([abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]),i,j])
        edgeset = []
        heapq.heapify(heap)
        while len(set(group.values())) > 1:
            weight,s,e = heapq.heappop(heap)
            if group[s] != group[e]:
                v1 = group[s]
                v2 = group[e]
                for key,v in list(group.items()):
                    if v == v2:
                        group[key] = v1
                edgeset.append(weight)
        return sum(edgeset)
                

