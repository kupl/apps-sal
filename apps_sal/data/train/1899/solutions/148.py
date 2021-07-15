class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        def get_poss(i, j, val=1):
            poss = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            poss = [(x, y) for x, y in poss if x >= 0 and x < m and y >= 0 and y < n
                    and A[x][y] == val]
            return poss
        
        def expand(i, j):
            A[i][j] = '#'
            poss = get_poss(i, j)
            for x, y in poss:
                expand(x, y)
            
        found_first = False
        boundaries = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if not found_first:
                        found_first = True
                        expand(i, j)
                    else:
                        #if get_poss(i, j, 0):
                        boundaries.append((i, j))
        
        def bfs(boundaries):
            recorder = set(boundaries)
            depth = 0
            roots = boundaries        
            while roots:
                next_level = []
                for x, y in roots:
                    poss1 = get_poss(x, y, '#')
                    if poss1:
                        return depth
                    poss = get_poss(x, y, 0)
                    for pos in poss:
                        if pos not in recorder:
                            recorder.add(pos)
                            next_level.append(pos)
                depth += 1
                roots = next_level
        return bfs(boundaries)

