class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # DFS: O(N^2) Time, O(N) Space
        # Tricky: [[1,1,0],[1,1,0],[0,0,1]], [0,1,2] -> If we remove 0, 1 can still infect 0 and we end up with 3 infected nodes. If we remove 2, we end up with 2 infected nodes -> SO we cant remove the node with the highest number of neighbors
        # New algorithm: We need to know which nodes are in the same component -> then no point in removing them since the other nodes would still infect it eventually
        
        # 1. Color each component
        # colors[node] = the color of this node.
        sizeComponents = defaultdict(int)
        nodesToComponents = defaultdict(int)
        c = 0
        def dfs(node, c):
            sizeComponents[c] += 1
            nodesToComponents[node] = c
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] == 1 and node != neighbor:
                    if neighbor not in nodesToComponents:
                        dfs(neighbor, c)
                        
                    
        for node in range(len(graph)):
            if node not in nodesToComponents:
                dfs(node, c)
                c += 1
        
        # 2. Map initial node to the size of their components
        # initialComponents = defaultdict(int)
        # for node in initial:
        #     component = nodesToComponents[node]
        #     initialComponents[node] = sizeComponents[component]
        
        # 2. Apparently, the question wants you to find which nodes in initial are in unique components
        initialComponents = defaultdict(int)
        for node in initial:
            component = nodesToComponents[node]
            initialComponents[component] += 1
            
        # 3. Find node with unique component, i.e. size of component == 1
        res = float('inf')
        for node in initial:
            component = nodesToComponents[node]
            size = sizeComponents[component]
            if initialComponents[component] == 1: # if this is the only
                if res == float('inf'):
                    res = node
                elif size > sizeComponents[nodesToComponents[res]]:
                    res = node
                elif size == sizeComponents[nodesToComponents[res]] and node < res:
                    res = node

        return res if res < float('inf') else min(initial)    
