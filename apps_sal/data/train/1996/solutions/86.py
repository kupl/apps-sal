class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unsafe_nodes = set()
        
        safe_nodes = set()
        
        def dfs(node, visited):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in unsafe_nodes:
                    unsafe_nodes.add(node)
                    return False
                if neighbor in safe_nodes:
                    continue
                if not dfs(neighbor, visited):
                    unsafe_nodes.add(node)
                    return False
     
            safe_nodes.add(node)
            return True
        
        safe = []
        for i in range(len(graph)):
            if dfs(i,set()):
                safe.append(i)
                
        return safe
