class Solution:
    def reachableNodes(self, edges, M, N):
        \"\"\"
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        \"\"\"
        adjacency = defaultdict(set)                    # map node to set of (nbor, number of nodes on edge)
        subdivisions = {}                               # map an edge to (number of nodes on edge, visited nodes)

        for a, b, intermediate in edges:
            subdivisions[(a, b)] = [intermediate, 0]
            subdivisions[(b, a)] = [intermediate, 0]
            adjacency[a].add((b, intermediate))
            adjacency[b].add((a, intermediate))

        queue = [(0, 0)]                                # (steps taken, node)
        visited = set()

        while queue and len(visited) < N:
            steps, node = heapq.heappop(queue)
            if node in visited:                         # already visited with lower or same steps
                continue
            visited.add(node)

            for nbor, distance in adjacency[node]:      # visit as many nodes as possible along this edge
                subdivisions[(node, nbor)][1] = min(distance, M - steps)

                if steps + distance + 1 <= M:           # visited all node on edge, add nbor to queue
                    heapq.heappush(queue, (steps + distance + 1, nbor))

        result = len(visited)                           # all nodes
        for (a, b), (distance, covered) in subdivisions.items():
            if a < b:
                result += min(distance, covered + subdivisions[(b, a)][1])  # sum edge nodes from both sides

        return result  
    
    
    def reachableNodes_(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(list)
        n = N 
        for i, j, ns in edges:
            if not ns:
                graph[i].append(j)
                graph[j].append(i)
                continue
            u = i
            v = n
            for _ in range(ns):
                graph[u].append(v)
                graph[v].append(u)
                u = v
                n += 1
                v = n
            v -= 1
            graph[v].append(j)
            graph[j].append(v)
        visited = {0}
        q = collections.deque([(0, 0)]) # node, move
        while q:
            for _ in range(len(q)):
                node, move = q.popleft()
                visited.add(node)
                if move == M:
                    continue
                for nxt in graph[node]:
                    if nxt not in visited:
                        q.append([nxt, move + 1])
        return len(visited)
                    
        
        
