class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        islands = [set(), set()]
        stack = []
        index = -1
        
        # build islands
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0 or (i, j) in islands[0] or (i, j) in islands[1]: continue
                
                index += 1
                stack.append((i, j))
                islands[index].add((i, j))
                
                while stack:
                    r, c = stack.pop()
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(A) and 0 <= nc < len(A[0]) \\
                        and A[nr][nc] == 1 and (nr, nc) not in islands[index]:
                            stack.append((nr, nc))
                            islands[index].add((nr, nc))
        
        import collections
        queue = collections.deque()
        visited = set()
        
        for r, c in islands[0]: queue.appendleft((r, c, 0))
            
        while queue:
            r, c, dist = queue.pop()
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in islands[1]: return dist
                
                if 0 <= nr < len(A) and 0 <= nc < len(A[0]) \\
                and A[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.appendleft((nr, nc, dist+1))
                    visited.add((nr, nc))
        
