class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 0:
            return True
        seen = {}
        adj = {i: [] for i in range(N+1) }
        for edge in dislikes: 
            #print('adj  ', adj, 'edge.. ', edge)
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

      
        def try_marking_all_edges(seen, node, adj, color) -> bool:
            if node in seen:
                return seen[node] == color
            seen[node] = color
            #print(\"try_marking_all_edges()\", node, \"->\", adj[node], \" seen \", seen)
            other_group = color ^ 1
            for a in adj[node]:
                if not try_marking_all_edges(seen, a, adj, other_group):
                    return False
            return True
    
        for node in adj:
            if node not in seen:
                if not try_marking_all_edges(seen, node, adj, 0):
                    return False
            if not try_marking_all_edges(seen, node, adj, seen[node]):
                return False
        return True  

            
            
    def possibleBipartition3(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 0:
            return True
        seen = {}
        adj = {i: [] for i in range(N+1) }
        for edge in dislikes: 
            ##print('adj  ', adj, 'edge.. ', edge)
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        def try_marking_all_edges(seen, node, adj) -> bool:
            #print(\"try_marking_all_edges()\", node, \"->\", adj[node])
            other_group = 2 if seen[node] == 1 else 1
            for a in adj[node]:
                if a not in seen:
                    seen[a] = other_group
                    continue
                if seen[a] != other_group:
                    return False
            return True
     
        print('adj  ', adj) 
     
        for edge in dislikes:
            print(edge, \"->\", seen)
            if not edge[0] in seen and not edge[1] in seen:
                seen[edge[0]] = 1
                seen[edge[1]] = 2
            elif edge[0] in seen and not edge[1] in seen:
                first_group = seen[edge[0]]
                seen[edge[1]] = 2 if first_group == 1 else 1
            elif edge[1] in seen and not edge[0] in seen:
                first_group = seen[edge[1]]
                seen[edge[0]] = 2 if first_group == 1 else 1
            else:
                if seen[edge[0]] == seen[edge[1]]:
                    return False
            if not try_marking_all_edges(seen, edge[0], adj): 
                return False
            if not try_marking_all_edges(seen, edge[1], adj):
                return False
            #print(edge, \"->>> \", seen)   


        return True    
            
            
        
    
    def possibleBipartition2(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 0:
            return True
        seen = {}
        for edge in dislikes: 
            if not edge[0] in seen and not edge[1] in seen:
                seen[edge[0]] = 1
                seen[edge[1]] = 2
            elif edge[0] in seen and not edge[1] in seen:
                first_group = seen[edge[0]]
                seen[edge[1]] = 2 if first_group == 1 else 1
            elif edge[1] in seen and not edge[0] in seen:
                first_group = seen[edge[1]]
                seen[edge[0]] = 2 if first_group == 1 else 1
            else:
                if seen[edge[0]] == seen[edge[1]]:
                    return False
        return True
                
            
        
        
