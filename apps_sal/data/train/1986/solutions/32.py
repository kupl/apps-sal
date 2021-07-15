class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        perms = [2 ** i for i in range(n-1, -1, -1)]
        
        end = start ^ 1
        
        visited = set()
        path = []
        
        def dfs(node):
            if node == end:
                path.append(node)
                return True
            
            if node in visited: return False
            
            visited.add(node)
            
            for perm in perms:
                if dfs(node ^ perm):
                    path.append(node)
                    return True
            return False
        
        dfs(start)
        return reversed(path)
