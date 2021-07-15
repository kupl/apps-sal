class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        #insight: check if connected, by DFS with both parties
        #if not, return -1, if so, then a tree may be possible
        
        # treat generally connected groups as single nodes
        # for each person, if DFS possible, then simply subtract unnecessary ones
        
#         # union join
#         count = 1
        
#         group = {}
        
#         for t, u, v in edges:
#             if t == 3:  # general links
#                 if u in group:
#                     v = group[u]
#                 elif v in group:
#                     u = group[v]
#                 else:  # new node
#                     group[u] = count
#                     group[v] = count
#                     count += 1
        
        
#         print(group)
        
#         return 0
                    
        
        # construct both graph
        from collections import defaultdict
        gboth = defaultdict(list)
        
        edge_counts = defaultdict(int)
        for t, u, v in edges:
            edge_counts[t] += 1
            if t == 3:
                gboth[u].append(v)
                gboth[v].append(u)
                
        print(gboth)
        
        group = {}
        nodes = set(range(1, n+1))
        seen = set()
        count = 1
        
        # print(nodes)
        
        def dfs(node, gnum):
            if node not in seen:
                seen.add(node)
                if node in nodes:
                    nodes.remove(node)
                group[node] = gnum
                for v in gboth[node]:
                    dfs(v, gnum)
        
        while nodes:
            dfs(nodes.pop(), count)
            count += 1
        count -= 1 # now it reps number of clusters
        
        print(group)
        print(\"edge couts\", edge_counts)
        # construct graphs for A & B, see if both possible.
        
        graphA = defaultdict(list)
        graphB = defaultdict(list)
        graphs = {1: graphA, 2: graphB}
        
        for t, u, v in edges:
            if group[u] != group[v]:
                if t == 1:
                    graphA[group[u]].append(group[v])
                    graphA[group[v]].append(group[u])
                elif t == 2:
                    graphB[group[u]].append(group[v])
                    graphB[group[v]].append(group[u])
        
        print(graphA, graphB)
        
        def dfs_a(node, person):
            if node not in seen:
                seen.add(node)
                
                for target in graphs[person][node]:
                    dfs_a(target, person)
        
        for i in range(1, 3):
            seen.clear()
            dfs_a(1, i)
            if len(seen) != count: # not connected
                print(\"disc,\", seen, count)
                return -1
        else:
            general_edges = edge_counts[3] - (n - count)
            a_edges = edge_counts[1] - count + 1
            b_edges = edge_counts[2] - count + 1
            return general_edges + a_edges + b_edges
