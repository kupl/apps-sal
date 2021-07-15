class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        \"\"\"
        Find the sum of distances between each node and all the other nodes
        \"\"\"
        
        # Edge case 1: There are no nodes given
        if N <= 1:
            return [0]
            
        # Edge case 2: There are no edges given
        if not edges:
            return [0]
        
        
        # Build adjacency list
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        
        count = [1] * N
        ans = [0] * N
        
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
            
        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
        
        # Method 1: 
        
        
#         # Method 2: Brute force method - O(N^2)
#         # For each node, use BFS 
#         for node in range(N):
#             # print(node)
#             visited = set()
#             queue = [node]
#             num = 0
#             depth = 0
            
#             while queue:
#                 length = len(queue)
                
#                 # Add elements to queue at each depth
#                 for i in range(length):
#                     vertex = queue.pop(0)
                    
#                     if vertex not in visited:
#                         visited.add(vertex)
#                         queue.extend(adj_list[vertex]-visited)  
                
#                 num += length * depth 
#                 depth += 1
            
#             ans.append(num)
        
        return ans
    
    
    def get_adjacency_list(self, edges) -> dict:
        \"\"\"
        Build adjacency list of undirected tree (graph)
        \"\"\"
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
#         adj_list = {}
        
#         for edge in edges:
#             node1 = edge[0]
#             node2 = edge[1]
#             # print(node1, node2)
            
#             if node1 not in adj_list:
#                 adj_list[node1] = set([node2])
#             else:
#                 adj_list[node1].add(node2)
                
#             if node2 not in adj_list:
#                 adj_list[node2] = set([node1])
#             else:
#                 adj_list[node2].add(node1)
                
#         return adj_list
