class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        \"\"\"
        sets, edges = [], []
        res = []

        for i in range(len(points)):
            sets.append([i])
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i,j,val))
        def custom_sort(t):
            return t[2]
        edges.sort(key=custom_sort)
        #print(edges); print(sets)
        
        for (u,v,cost) in edges:
            for i in range(len(sets)):
                if u in sets[i]:
                    setu = i
                    break
            for i in range(len(sets)):
                if v in sets[i]:
                    setv = i
                    break
            if setu != setv:
                w1 = sets[setu]
                w2 = sets[setv]
                res.append((u,v,cost))
                [w1.append(x) for x in w2 if x not in w1]
                sets = sets[:setv]+sets[setv+1:]
        
        sum = 0
        for e in res:
            sum += e[2]
        return sum
        \"\"\"
        edges = [[None] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges[i][j] = val
                edges[j][i] = val
        
        cost = 0
        min_heap = [(0, 0)]
        visited = set()
        while len(min_heap):
            min_node = heapq.heappop(min_heap)
            if min_node[1] in visited: continue
            vertex = min_node[1]
            weight = min_node[0]
            cost += weight
            visited.add(vertex)
            #print('visted vertex is ', vertex, 'cost is', weight, 'total', cost, 'cur_min_heap', min_heap)
            for neigh in range(len(edges[vertex])):
                if neigh not in visited:
                    heapq.heappush(min_heap, (edges[vertex][neigh], neigh))
        
        return cost
