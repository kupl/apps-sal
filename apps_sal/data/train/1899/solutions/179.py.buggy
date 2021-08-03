class Solution:
    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        
        # Mark island1 and island2
        visited = set()
        islands = []
        for i in range(m):
            for j in range(n):
                if A[i][j] != 1 or (i, j) in visited:
                    continue
                    
                seen = {(i, j)}
                self.__class__.dfs(A, i, j, seen)

                visited |= seen    # union
                islands.append(copy.deepcopy(seen))
                    
        print(islands)
        source, target = islands
        
        # Flood fill
        queue = list(source)
        visited = source
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                print(i, j)
                if (i, j) in target:
                    return step - 1
                
                for delta in self.__class__.DIRS:
                    x, y = i + delta[0], j + delta[1]
                    if x < 0 or x >= m or \\
                            y < 0 or y >= n:
                        continue
                    if (x, y) in visited:
                        continue
                        
                    visited.add((x, y))
                    queue.append((x, y))
            step += 1
                    
        return -1
    
    @classmethod
    def dfs(cls, A, i, j, visited):
        m, n = len(A), len(A[0])
        
        for delta in cls.DIRS:
            x, y = i + delta[0], j + delta[1]
            if x < 0 or x >= m or \\
                    y < 0 or y >= n:
                continue
                
            if A[x][y] != 1 or (x, y) in visited:
                continue
            
            visited.add((x, y))
            cls.dfs(A, x, y, visited)

        
