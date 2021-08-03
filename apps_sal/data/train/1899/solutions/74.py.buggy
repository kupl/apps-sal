class Solution:
    \"\"\"
    [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [0,0,1,1,1],
        [1,0,0,1,1],
        [1,1,1,0,1]]
    \"\"\"
    def shortestBridge(self, A: List[List[int]]) -> int:
        def is_valid(r, c):
            return 0 <= r < len(A) and 0 <= c < len(A[0])
        
        def dfs(r, c, island, visited):
            if A[r][c] == 0:
                return
            if (r, c) in visited:
                return
            dirs = [
                [0, 1],
                [0, - 1],
                [1, 0],
                [-1, 0]
            ]
            visited.add((r, c))
            is_border = False
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if (nr, nc) in visited:
                    continue
                # only record border coordinates
                if not is_valid(nr, nc):
                    is_border = True
                    
                    continue
                if A[nr][nc] == 0:
                    is_border = True
                    
                    continue
                dfs(nr, nc, island, visited)
            if is_border:
                island.append((r, c))
            return
        
        islands = []
        visited = set()
        
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1 and (r, c) not in visited:
                    island = []
                    dfs(r, c, island, visited)
                    islands.append(island)
        
        def get_shortest_dist(islands1, islands2):
            min_dist = len(A)
            for i in range(len(islands1)):
                for j in range(len(islands2)):
                    r_dist = abs(islands1[i][0] - islands2[j][0])
                    c_dist = abs(islands1[i][1] - islands2[j][1])
                    min_dist = min(min_dist, r_dist + c_dist)
            return min_dist - 1
        
        return get_shortest_dist(islands[0], islands[1])
        
            
