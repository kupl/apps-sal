class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        
        N = len(A)
        def neighbors(r, c):
            for dr, dc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= dr < N and 0 <= dc < N:
                    yield dr, dc
        
        def get_components():
            visited = set()
            island = []
            for r in range(N):
                for c in range(N):
                    if A[r][c] == 1 and (r, c) not in visited:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            i, j = stack.pop()
                            for dr, dc in neighbors(i, j):
                                if A[dr][dc] == 1 and (dr, dc) not in seen:
                                    stack.append((dr, dc))
                                    seen.add((dr, dc))
                        island.append(seen)
                        visited |= seen
            return island
    
        island = get_components()
        queue = collections.deque([(node, 0) for node in island[0]])
        visited=island[0]
        while queue:
            node, d = queue.popleft()
            if node in island[1]:
                return d-1
            for r, c in neighbors(*node):
                if (r, c) not in visited:
                    queue.append(((r,c), d+1))
                    visited |= set([(r, c)])
        
        \"\"\"
        nrow, ncol = len(A), len(A[0])
        
        def is_valid(nr, nc):
            if 0 <= nr < nrow and 0 <= nc < ncol:
                return True
            return False
        
        def get_components():
            visited = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in visited:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            r1, c1 = stack.pop()
                            for nei in ((r1-1, c1), (r1+1, c1), (r1, c1-1), (r1, c1+1)):
                                if is_valid(nei[0], nei[1]) and A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        visited = visited.union(seen) # visited |= seen
                        components.append(seen)
            return components
        
        components = get_components()
        print (components)
        \"\"\"

            
        
                    
