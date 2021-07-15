class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        groups = [a for a in range(len(points))]
        for index_a in range(len(points)):
            for index_b in range(index_a+1, len(points)):
                edge = (index_a, index_b, abs(points[index_a][0] - points[index_b][0]) + abs(points[index_a][1] - points[index_b][1]))
                edges.append(edge)
        edges.sort(key = lambda a:a[2])
        
        
        def find(a):
            return a if groups[a] == a else find(groups[a])
        
        def union(a, b):
            group_a = find(a)
            group_b = find(b)
            if group_a != group_b:
                return group_a, group_b
            return 
        
        sum = 0
        while len(set(groups)) != 1:
            edge = edges.pop(0)
            merged = union(edge[0], edge[1])
            if merged is not None:
                groups = [merged[1] if x == merged[0] else x for x in groups]
                sum += edge[2]
        return sum
