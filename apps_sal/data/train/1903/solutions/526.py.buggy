class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # APPROACH 1 - My Kruskal trial
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
        
        # APPRTOACH 2 - MIN_HEAP/Prim
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
            #print('cur_min_heap', min_heap)
            min_node = heapq.heappop(min_heap)
            if min_node[1] in visited: continue
            vertex = min_node[1]
            weight = min_node[0]
            cost += weight
            visited.add(vertex)
            #print('visted vertex is', vertex, '; cost is', weight, '; total', cost, '; cur_min_heap', min_heap)
            for neigh in range(len(edges[vertex])):
                if neigh not in visited:
                    heapq.heappush(min_heap, (edges[vertex][neigh], neigh))
        
        return cost
        \"\"\"
        
        #APPROACH 3 - Prim
        ##### https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/854251/Python-Kruskals-algo-implemented-with-array-easy-to-understand
        visited = []
        l = len(points)
\t\t# points are node in graph, and there're at most l^2 edges.
        edges = []
\t\t# Get all the edges, and each is represented with [cost, two_ends]
        for i in range(l):
            for j in range(i+1, l):
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                edges.append([x + y, [i,j]])
\t\t# Sort the edges by their cost
        edges.sort(key = lambda x:x[0])
        result = 0
        nodes = [0]* l
\t\t# union connected nodes,  mark the node with mark = 1, and for each separated group, we use mark = 2 /3 ...
        mark = 1
        for e in edges:
\t\t   # Two end nodes
            i = e[1][0]
            j = e[1][1]
\t\t\t# Both are not marked, so are not connected at all, and can be marked with new mark
            if nodes[i] == 0 and nodes[j] == 0:
                
                nodes[i] = mark
                nodes[j] = mark
                mark += 1
                result += e[0]
\t\t\t# One of them is marked, so connected to some connected components
            elif nodes[i] == 0:
                nodes[i] = nodes[j]
                result += e[0]
\t\t\t# One of them is marked, so connected to some connected components
            elif nodes[j] == 0:
                nodes[j] = nodes[i]
                result += e[0]
\t\t\t# Both of them are marked, so are already connected to some connected components;
\t\t\t# if they are in the same connected component, this edge cannot be added; Or there'd be a cycle
\t\t\t# If they are in different c.c., they should be united, so we need to update the mark on the nodes. And the method is to loop all the nodes, change the mark for all the nodes in one c.c. to the mark of the other c.c.
            else:
                if nodes[i] != nodes[j]:
                    result += e[0]
                    target = nodes[i]
                    source = nodes[j]
                    for index in range(l):
                        if nodes[index] == source:
                            nodes[index] = target
        return result
        
        
