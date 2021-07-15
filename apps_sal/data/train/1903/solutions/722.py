class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        cost_map = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                cost_map[(i, j)] = cost
        
        graph = []
        for key, value in cost_map.items():
            graph.append([key[0], key[1], value])        
        
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(city1, city2):
            root1 = find(city1)
            root2 = find(city2)
            if root1 == root2:
                return False # Cycle
            parent[root2] = root1 # Join roots
            return True
            
        #Keep track of disjoint sets. Initially each city is its own set.
        parent = {city:city for city in range(0, len(points))}
        #Sort connections so we are always picking minimum cost edge.
        graph.sort(key=lambda x:x[2])
        totalCost = 0
        for city1, city2, cost in graph:
            if union(city1, city2):
                totalCost += cost
        
        # Check that all cities are connected
        root = find(len(points)-1)
        for i in range(0, len(points)):
            if find(i) == root:
                continue
            else:
                return -1
        return totalCost
